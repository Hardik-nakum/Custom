# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference")
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
    ], string="Gender")
    active = fields.Boolean(string="Active", default=True)
