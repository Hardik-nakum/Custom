from odoo import fields, models, api


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag model"

    name = fields.Char(string="Name", required=True, default="Unknown")
