from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "estate property model"

    name = fields.Char(string="Title", required=True, default="Unknown")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode", compute='search_count')
    date_availability = fields.Date(string="Available From", copy=False,
                                    default=datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default="2")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)", compute='_compute_data')
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    property_type_id = fields.Many2one("estate.property.type", "Property Type")
    property_type = fields.Char("Property Type")
    buyer = fields.Many2one("res.partner", "Buyer", copy=False)
    seller = fields.Many2one("res.users", "Seller", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ])
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        string='State',
        default="new",
        copy=False,
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ])

    @api.model
    def create(self, vals):
        vals["name"] = "demo"
        vals["selling_price"] = "300000"
        res = super(EstateProperty, self).create(vals)
        return res

    def write(self, vals):
        res = super(EstateProperty, self).write(vals)
        return res

    def copy(self, default={}):
        default['postcode'] = None
        res = super(EstateProperty, self).copy(default=default)
        return res

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        res = super(EstateProperty, self).search(args, order='name desc')
        return res

    @api.depends()
    def search_count(self):
        count = super(EstateProperty, self).search_count([('tag_ids', '=', 'cozy')])
        self.postcode = count

    # @api.onchange("buyer")
    # def onchange_type(self):
    #     print("On Change")

    @api.depends('living_area', 'bedrooms', 'garden_area')
    def _compute_data(self):
        for record in self:
            record.garden_area = record.living_area * record.bedrooms

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 500:
                raise ValidationError(_("expected_price error"))

    @api.model
    def default_get(self, x=[]):
        rec = super(EstateProperty, self).default_get(x)
        print("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", rec)
        return rec

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        # optimize out the default criterion of ``ilike ''`` that matches everything
        if not (name == '' and operator == 'ilike'):
            args += ['|', (self._rec_name, operator, name), ('living_area', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
