from odoo import models, fields

class SaleTeamHierarchy(models.Model):
    _name = 'sale.team.hierarchy'
    _description = 'Sales Team Hierarchy'

    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('sale.team.hierarchy', string='Parent Hierarchy')
    team_ids = fields.One2many('crm.team', 'hierarchy_id', string='Sales Teams')
