
from .test_parent_common import TestParentCommon


class TestParent(TestParentCommon):

    def setUp(self):
        super(TestParent, self).setUp()

    def test_case_1_parent(self):
        parents = self.vm_parent.search([])
        vals = {
            'name': self.env.ref('viseducat_core.vm_res_partner_31').id,
            'user_id': self.env.ref('viseducat_parent.user_parent').id,
            'relationship_id': self.env.ref('viseducat_parent.vm_parent_relationship_1').id,
            'mobile': 8334845,
        }
        new_parent = self.vm_parent.create(vals)
        new_parent.create_parent_user()
        student = self.env.ref('viseducat_parent.user_parent').id
        val = {'mobile': 77777777}
        self.vm_parent.search([('user_id', '=', student)]).write(val)

        for parent in parents:
            parent._onchange_name()

        self.vm_parent.search([('user_id', '=', student)]).unlink()

    def test_case_2_student(self):
        vals = {
            'user_id': self.env.ref('viseducat_parent.user_parent').id,
            'partner_id': self.env.ref('viseducat_parent.res_partner_33').id,
            'name': 'nikul',
            'last_name': 'ahir',
            'gender': 'm',
            'birth_date': '2009-01-01',
            'mobile': '73482383624',
            'email': 'nik@gmail.com',
            'parent_ids': [(6, 0, [self.env.ref('viseducat_parent.vm_parent_1').id])],
        }

        self.vm_student.create(vals)
        vals.update({
            'name': 'NIK AHiR',
            'parent_ids': [(6, 0, [self.env.ref('viseducat_parent.vm_parent_1').id])],
        })
        self.vm_student.write(vals)
        self.vm_student.unlink()

    def test_case_3_subject_registartion(self):
        vals = {
            'student_id': self.env.ref('viseducat_core.vm_student_1').id,
            'course_id': self.env.ref('viseducat_core.vm_course_2').id,
            'batch_id': self.env.ref('viseducat_core.vm_batch_1').id,
        }
        self.subject_registration.create(vals)
        self.subject_registration.write(vals)
