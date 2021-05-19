
from odoo import models, fields, api, _


class VmCourse(models.Model):
    _name = "vm.course"
    _inherit = "mail.thread"
    _description = "Course"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=16, required=True)
    parent_id = fields.Many2one('vm.course', 'Parent Course')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'),
         ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('vm.subject', string='Subject(s)')
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")
    department_id = fields.Many2one(
        'vm.department', 'Department',
        default=lambda self:
        self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)
    student_count = fields.Integer(compute='student_count_compute', string='Number of Student')
    child_course_count = fields.Integer(compute='_child_course_count_compute', string='Number of Child Course')
    subject_count = fields.Integer(compute='_subject_count_compute', string='Number of Subject')
    batch_count = fields.Integer(compute='_batch_count_compute', string='Number of Batch')
    color = fields.Integer("Color Index", default=0)

    # sale quotation onboarding
    course_onboarding_course_layout_state = fields.Selection([('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")], string="State of the onboarding course layout step", default='not_done')
    course_onboarding_batch_layout_state = fields.Selection([('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done"), ('closed', "Closed")], string="State of the batch onboarding panel", default='not_done')
    course_onboarding_subject_layout_state = fields.Selection([('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done"), ('closed', "Closed")], string="State of the subject onboarding panel", default='not_done')



    _sql_constraints = [
        ('unique_course_code',
         'unique(code)', 'Code should be unique per course!')]



    def student_count_compute(self):
        self.student_count = 2
        action = self.env.ref('viseducat_core.act_open_vm_student_view_2').read()[0]
        # action['domain'] = [('student_id', 'in', self.ids)]
        return action

    def _child_course_count_compute(self):
        self.child_course_count = 2
        action = self.env.ref('viseducat_core.act_open_vm_student_view_2').read()[0]
        # action['domain'] = [('student_id', 'in', self.ids)]
        return action

    def _subject_count_compute(self):
        self.subject_count = 2
        action = self.env.ref('viseducat_core.act_open_vm_student_course_view').read()[0]
        # action['domain'] = [('student_id', 'in', self.ids)]
        return action

    def _batch_count_compute(self):
        self.batch_count = 2
        action = self.env.ref('viseducat_core.act_open_vm_batch_view').read()[0]
        # action['domain'] = [('student_id', 'in', self.ids)]
        return action


    # def get_and_update_course_dashboard_onboarding_state(self):
    #     return self.get_and_update_onbarding_state(
    #         'course_onboarding_course_layout_state',
    #     )

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Courses'),
            'template': '/viseducat_core/static/xls/vm_course.xls'
        }]