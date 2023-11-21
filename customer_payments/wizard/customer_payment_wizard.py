from odoo import models, fields, _
from odoo.exceptions import Warning, ValidationError


class CustomerWiseReportWizard(models.TransientModel):
    _name = "customer.payment.report.wizard"
    _description = "Customer Wise Payment"

    fr_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    def action_print_report(self):
        # fetch from and to date
        x = self.fr_date.strftime('%Y-%m-%d 00:00:00')
        y = self.to_date.strftime('%Y-%m-%d 23:59:59')
        if self.fr_date > self.to_date:
            raise Warning(_("From Date Is GreaterThan To Date !"))
        else:
            condition = '''and sml.date between '%s' AND '%s'
                   ''' % (x, y)
            query = """
                SELECT
                    move.partner_id,
                    partner.name AS partner_name,
                    MIN(move.create_date) AS first_sales_date,
                    COUNT(move.id) AS total_sale_count,
                    pmt.amount AS total_paid_amount,
                    SUM(move.amount_total) AS total_amount,
                    (SUM(move.amount_total) - pmt.amount) AS balance_amount
                FROM
                    account_move AS move
                LEFT JOIN res_partner AS partner ON move.partner_id = partner.id
                LEFT JOIN (
                    SELECT
                        pmt.partner_id,
                        SUM(pmt.amount_company_currency_signed) AS amount
                    FROM
                        account_payment AS pmt
                    WHERE
                        pmt.payment_type = 'inbound'
                    GROUP BY
                        pmt.partner_id
                ) AS pmt ON move.partner_id = pmt.partner_id
                WHERE
                    move.move_type = 'out_invoice'
                     AND DATE(move.date) BETWEEN '%s' AND '%s'
                GROUP BY
                    move.partner_id, partner.name, pmt.amount
            """ % (x, y)

        self._cr.execute(query)
        # place query values in the variable payments
        payments = self._cr.dictfetchall()
        print(payments)

        # if nothing to display this msg shows
        if not payments:
            raise ValidationError("Nothing To Print !")
        data = {
            'ids': self.ids,
            'model': self._name,
            'date_from': self.fr_date.strftime('%d/%m/%Y'),
            'date_to': self.to_date.strftime('%d/%m/%Y'),
            'vals': payments
        }
        print('data', data)
        # pass vals to report template

        action = self.env.ref('customer_payments.record_customer_payment_report_print').report_action(self, data=data)

        return action
