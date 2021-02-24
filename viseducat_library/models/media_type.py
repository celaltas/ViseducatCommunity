from odoo import models, fields


class VmMediaType(models.Model):
    _name = "vm.media.type"
    _description = "Media Type"

    name = fields.Char('Name', size=64, required=True)
    code = fields.Char('Code', size=64, required=True)

    _sql_constraints = [
        ('unique_media_type_code',
         'unique(code)', 'Code should be unique per media type!')]