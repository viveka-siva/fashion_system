from odoo import models, fields


class NameContent(models.TransientModel):
    _name = 'name.conversion'

    first_name = fields.Char('First Name:')
    last_name = fields.Char('Last Name:')

    def concat(self):
        active_id = self.env.context.get('active_id', False)
        active_ids = self.env.context.get('active_ids', False)
        active_model = self.env.context.get('active_model', False)
        concatenate = self.env['order'].browse(active_id)
        joint_name = self.first_name + " " + self.last_name
        concatenate.write({'name': joint_name})







