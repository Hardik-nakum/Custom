from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    phone = fields.Char(string="Phone")
    average = fields.Char(string="Average", compute="_compute_average")

    @api.onchange("partner_id")
    def onchange_type(self):
        for record in self:
            if record.partner_id.phone:
                record.phone = record.partner_id.phone
            else:
                record.phone = record.partner_id.mobile

    @api.depends('tax_totals_json')
    def _compute_average(self):
        for record in self:
            record.average = 0
            if len(record.order_line) != 0:
                record.average = record.amount_total / len(record.order_line)


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    profit = fields.Char('Profit', compute="_compute_profit")
    type = fields.Selection('Type', related='product_id.detailed_type')

    @api.depends('price_unit', 'product_id')
    def _compute_profit(self):
        for record in self:
            record.profit = record.product_id.lst_price - record.product_id.standard_price

    @api.depends('price_unit', 'product_id')
    @api.onchange("price_unit")
    def onchange_type(self):
        for record in self:
            record.profit = record.price_unit - record.product_id.standard_price

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['p_type'] = dict(self.fields_get(['type'], ['selection']).get('type').get('selection')).get(self.type)
        return res


class AccountMove(models.Model):
    _inherit = ['account.move.line']

    p_type = fields.Char(string='Product Type')
