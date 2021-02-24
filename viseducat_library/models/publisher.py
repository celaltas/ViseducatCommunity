from odoo import models, fields


class VmPublisher(models.Model):
    _name = "vm.publisher"
    _description = "Publisher"

    name = fields.Char('Name', size=20, required=True)
    address_id = fields.Many2one('res.partner', 'Address')
    media_ids = fields.Many2many('vm.media', string='Media(s)')