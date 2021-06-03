from odoo import models, fields, api


class FashionGarment(models.Model):
    _name = 'fashion.garment'
    name = fields.Char(string='Name')
    quantity = fields.Integer(string='Quantity')
    price = fields.Integer(string='Price')
    garment_type = fields.Selection([('t-shirt', 'T-Shirt'),
                                     ('shirt', 'Shrirt'),
                                     ('jeans', 'Jeans'),
                                     ('short', 'Short'),
                                     ('shoe', 'Shoe'),
                                     ])
    brand = fields.Selection([('nike', 'Nike'),
                              ('levis', 'Levis'),
                              ('adidas', 'Adidas'),
                              ('wrogn', 'Wrogn'),
                              ('pepe', 'Pepe'),
                              ])
    orders_id = fields.One2many('order.line','garment_id', string="Record List")

