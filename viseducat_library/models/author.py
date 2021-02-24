from odoo import models, fields


class VmAuthor(models.Model):
    _name = "vm.author"
    _description = "Media Author"

    name = fields.Char('Name', size=128, required=True)
    address = fields.Many2one('res.partner', 'Address')
    media_ids = fields.Many2many('vm.media', string='Media(s)')