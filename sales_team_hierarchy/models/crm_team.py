from odoo import models, fields

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    hierarchy_id = fields.Many2one('sale.team.hierarchy', string='Sales Team Hierarchy')