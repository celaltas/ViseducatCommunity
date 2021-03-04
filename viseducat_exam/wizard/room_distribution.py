from odoo import models, api, fields, exceptions, _


class VmRoomDistribution(models.TransientModel):
    """ Exam Room Distribution """
    _name = "vm.room.distribution"
    _description = "Room Distribution"

    @api.depends('student_ids')
    def _compute_get_total_student(self):
        for record in self:
            total_student = 0
            if record.student_ids:
                total_student = len(record.student_ids)
            record.total_student = total_student

    @api.depends('room_ids', 'room_ids.capacity')
    def _compute_get_room_capacity(self):
        for record in self:
            room_capacity = 0
            if record.room_ids:
                for room in record.room_ids:
                    room_capacity += (room.capacity or 0)
            record.room_capacity = room_capacity

    exam_id = fields.Many2one('vm.exam', 'Exam(s)')
    subject_id = fields.Many2one('vm.subject', 'Subject',
                                 related="exam_id.subject_id")
    name = fields.Char("Exam")
    start_time = fields.Datetime("Start Time")
    end_time = fields.Datetime("End Time")
    exam_session = fields.Many2one("vm.exam.session", 'Exam Session')
    course_id = fields.Many2one("vm.course", 'Course')
    batch_id = fields.Many2one("vm.batch", 'Batch')
    total_student = fields.Integer(
        "Total Student", compute="_compute_get_total_student")
    room_capacity = fields.Integer(
        "Room Capacity", compute="_compute_get_room_capacity")
    room_ids = fields.Many2many("vm.exam.room", string="Exam Rooms")
    student_ids = fields.Many2many("vm.student", String='Student')

    @api.model
    def default_get(self, fields):
        res = super(VmRoomDistribution, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        exam = self.env['vm.exam'].browse(active_id)
        session = exam.session_id
        reg_ids = self.env['vm.subject.registration'].search([('course_id', '=', session.course_id.id)])
        student_ids = []
        for reg in reg_ids:
            if exam.subject_id.subject_type == 'compulsory':
                student_ids.append(reg.student_id.id)
            else:
                for sub in reg.elective_subject_ids:
                    if sub.id == exam.subject_id.id:
                        student_ids.append(reg.student_id.id)

        student_ids = list(set(student_ids))
        total_student = len(student_ids)
        res.update({
            'exam_id': active_id,
            'name': exam.name,
            'start_time': exam.start_time,
            'end_time': exam.end_time,
            'exam_session': session.id,
            'course_id': session.course_id.id,
            'batch_id': session.batch_id.id,
            'total_student': total_student,
            'student_ids': [(6, 0, student_ids)],
        })
        return res

    def schedule_exam(self):
        attendance = self.env['vm.exam.attendees']
        for exam in self:
            if exam.total_student > exam.room_capacity:
                raise exceptions.AccessError(
                    _("Room capacity must be greater than total number \
                      of student"))
            student_ids = exam.student_ids.ids
            for room in exam.room_ids:
                for i in range(room.capacity):
                    if not student_ids:
                        continue
                    attendance.create({
                        'exam_id': exam.exam_id.id,
                        'student_id': student_ids[0],
                        'status': 'present',
                        'course_id': exam.course_id.id,
                        'batch_id': exam.batch_id.id,
                        'room_id': room.id
                    })
                    student_ids.remove(student_ids[0])
            exam.exam_id.state = 'schedule'
            return True




