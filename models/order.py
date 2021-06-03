from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'order'
    name = fields.Char(string='Name')
    order_date = fields.Date(string=' Order Date')
    quantity = fields.Integer(string='Quantity')
    total = fields.Integer(string='Total')
    price = fields.Integer(string='Price')
    orderlines_ids = fields.One2many('order.line','order_ids')
    # discount_per = fields.Integer(string="Discount = % :")

    def calculate_total(self):
        sum=0
        print(self)
        print(self.name)
        print(self.order_date)
        print(self.orderlines_ids)
        for rec in self.orderlines_ids:
            print(rec)
            print(rec.customer)
            print(rec.total)
            print(rec.quantity)
            sum += rec.total
        self.write({'total': sum})
        return True

    # def discount(self):
    #     dcount = ((self.total*self.discount_per)/100)
    #     self.write({'discount_per': self.total-dcount})
    #     return True




class OrderLine(models.Model):
    _name = 'order.line'
    customer = fields.Char(string="Name")
    total = fields.Integer(string='Total')
    quantity = fields.Integer(string='Quantity')
    price = fields.Integer(string='Price')
    garment_id = fields.Many2one('fashion.garment', string='Garment')
    order_ids = fields.Many2one('order', string='Order')
    garment_type = fields.Selection([('t-shirt', 'T-Shirt'),
                                     ('shirt', 'Shrirt'),
                                     ('jeans', 'Jeans'),
                                     ('short', 'Short'),
                                     ('shoe', 'Shoe'),
                                     ])







