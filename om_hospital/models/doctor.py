# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"

    name = fields.Char(string="Name", tracking=True)
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
    ], string="Gender")
    user_id = fields.Many2one("res.users", string="Related User")
