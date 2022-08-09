from odoo import api, fields, models


class TestModel(models.Model):
    _name = "test.model"
    _description = "test model"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    reference = fields.Text(string="Reference")
    dob = fields.Date(string="Birth Date")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
