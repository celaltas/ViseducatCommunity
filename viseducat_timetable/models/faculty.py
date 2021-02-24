from odoo import models, fields


class OpFaculty(models.Model):
    _inherit = "vm.faculty"

    session_ids = fields.One2many('vm.session', 'faculty_id', 'Sessions')

