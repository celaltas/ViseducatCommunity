from odoo import models, fields, api, _
from odoo.exceptions import ValidationError





class VmStudentCourse(models.Model):
    _name = "vm.student.course"
    _description = "Student Course Details"
    _rec_name = 'student_id'

    student_id = fields.Many2one('vm.student', 'Student', ondelete="cascade")
    course_id = fields.Many2one('vm.course', 'Course', required=True)
    batch_id = fields.Many2one('vm.batch', 'Batch', required=True)
    roll_number = fields.Char('Roll Number')
    subject_ids = fields.Many2many('vm.subject', string='Subjects')

    _sql_constraints = [
        ('unique_name_roll_number_id',
         'unique(roll_number,course_id,batch_id,student_id)',
         'Roll Number & Student must be unique per Batch!'),
        ('unique_name_roll_number_course_id',
         'unique(roll_number,course_id,batch_id)',
         'Roll Number must be unique per Batch!'),
        ('unique_name_roll_number_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Batch!'),
    ]


class VmStudent(models.Model):
    _name = "vm.student"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {"res.partner": "partner_id"}

    first_name = fields.Char('First Name', size=128, translate=True)
    middle_name = fields.Char('Middle Name', size=128, translate=True)
    last_name = fields.Char('Last Name', size=128, translate=True)
    birth_date = fields.Date('Birth Date')
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Blood Group')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ], 'Gender', required=True, default='m')
    nationality = fields.Many2one('res.country', 'Nationality')
    emergency_contact = fields.Many2one('res.partner', 'Emergency Contact')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    partner_id = fields.Many2one('res.partner', 'Partner',
                                 required=True, ondelete="cascade")
    user_id = fields.Many2one('res.users', 'User', ondelete="cascade")
    gr_no = fields.Char("GR Number", size=20)
    category_id = fields.Many2one('vm.category', 'Category')
    course_detail_ids = fields.One2many('vm.student.course', 'student_id',
                                       'Course Details',
                                     track_visibility='onchange')
    active = fields.Boolean(default=True)


    _sql_constraints = [(
        'unique_gr_no',
        'unique(gr_no)',
        'GR Number must be unique per student!'
    )]

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.middle_name:
            self.name = str(self.first_name) + " " + str(self.last_name)
        else:
            self.name = str(self.first_name) + str(self.middle_name) + str(self.last_name)

    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date>fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))

    def create_student_user(self):
        user_group = self.env.ref("base.group_portal") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name,
                    'partner_id': record.partner_id.id,
                    'login': record.email,
                    'groups_id': user_group,
                    'is_student': True,
                    'tz': self._context.get('tz'),
                })
                record.user_id = user_id





