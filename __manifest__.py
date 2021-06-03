# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fashion System',
    'version': '0.1',
    'summary': 'Sample case double for fashion',
    'description': """ Demo Practice
    """,
    'depends': ['base'],
    'data': [
        'wizard/discount.xml',
        'wizard/name.xml',
        'security/ir.model.access.csv',
        'views/garment.xml',
        'views/order.xml',
       ],
    'installable': True,
    'auto_install': False
}