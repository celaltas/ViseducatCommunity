from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmBatch(models.Model):
    _name = "vm.batch"
    _inherit = "mail.thread"
    _description = "Batch"

    code = fields.Char('Code', size=16, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('vm.course', 'Course', required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for rec in self:
            if rec.start_date >= rec.end_date:
                raise ValidationError(
                    _("End date cannot be set before start date."))


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['vm.course'].browse(lst)
            while courses.parent_id:
                lst.append(courses.parent_id.id)
                courses = courses.parent_id
            batches = self.env['vm.batch'].search([('course_id', 'in', lst)])
            return batches.name_get()
        return super(VmBatch, self).name_search(
            name, args, operator=operator, limit=limit)


    def action_save_onboarding_batch_step(self):
        course =self.env['vm.course'].search([], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_batch_layout_state')

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Batch'),
            'template': '/viseducat_core/static/xls/vm_batch.xls'
        }]

