from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"

    name = fields.Many2one("estate.property", string="Title", required=True)
    living_area = fields.Integer(string="Living Area", related="name.living_area")
    name_id = fields.Char(string="Id", default='2')

    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.name:
                name = str(record.id) + ' ' + record.name
            res.append((record.id, name))
        return res


