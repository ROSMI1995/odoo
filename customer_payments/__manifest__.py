# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Customer Payments',
    'author': 'Rosmi Thomas',
    'version': '1.0',
    'summary': 'customer payments details',
    'sequence': 10,
    'category': 'report',
    'description': 'customer wise  payments details',
    'depends': ['base', 'account'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/customer_payment_wizard.xml',
        'report/payment_report.xml',
        'report/payment_report_template.xml',
    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
