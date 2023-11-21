# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sales Team',
    'author': 'Rosmi Thomas',
    'version': '1.0',
    'summary': 'sales_team_hierarchy',
    'sequence': 10,
    'description': 'sales_team_hierarchy',
    'depends': ['base', 'crm', 'sale'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_team_hierarchy.xml',
    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
