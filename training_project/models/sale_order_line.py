from odoo import models, fields, api


class SaleOrderLIne(models.Model):
    _inherit = 'sale.order.line'
    total_amt = fields.Float(string='Total Amount')
