from odoo import models, fields, api


class VmAttendanceRegister(models.Model):
    _name = "vm.attendance.register"
    _inherit = ["mail.thread"]
    _description = "Attendance Register"
    _order = "id DESC"

    name = fields.Char(
        'Name', size=16, required=True, track_visibility='onchange')
    code = fields.Char(
        'Code', size=16, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'vm.course', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'vm.batch', 'Batch', required=True, track_visibility='onchange')
    subject_id = fields.Many2one(
        'vm.subject', 'Subject', track_visibility='onchange')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_attendance_register_code',
         'unique(code)', 'Code should be unique per attendance register!')]

    @api.depends('course_id')
    def onchange_course(self):
        if not self.course_id:
            self.batch_id = False
