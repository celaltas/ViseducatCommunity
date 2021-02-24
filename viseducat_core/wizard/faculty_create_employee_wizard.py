from odoo import models, fields


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.vm.faculty.employee'
    _description = "Create Employee and User of Faculty"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    def create_employee(self):
       for rec in self:
           active_id = self.env.context.get('active_ids', []) or []
           faculty = self.env['vm.faculty'].browse(active_id)
           faculty.create_employee()

           #grup işlemleri var geri dön