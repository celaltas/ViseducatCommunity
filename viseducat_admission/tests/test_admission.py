
import logging
from .test_admission_common import TestAdmissionCommon


class TestAdmission(TestAdmissionCommon):

    def setUp(self):
        super(TestAdmission, self).setUp()

    def test_case_1_admissions(self):
        admissions = self.vm_admission.search([])
        self.vm_admission._onchange_name()

        vals = {
            'name': 'AHIR',
            'first_name': 'Nikul',
            'middle_name': 'M',
            'last_name': 'Last',
            'application_number': self.env.ref(
                'viseducat_admission.seq_vm_admission').id,
            'birth_date': '2002-12-20',
            'course_id': self.env.ref('viseducat_core.vm_course_5').id,
            'batch_id': self.env.ref('viseducat_core.vm_batch_4').id,
            'phone': 32234234,
            'mobile': 93432,
            'email': 'nik.ahir@gmail.com',
            'state': 'submit',
            'gender': 'm',
            'register_id': self.env.ref(
                'viseducat_admission.vm_admission_register_3').id,
            'image': False
        }

        studnet_1 = self.vm_admission.create(vals)
        studnet_1.enroll_student()

        vals_2 = {
            'name': 'Ahir',
            'first_name': 'Nikul',
            'middle_name': 'M',
            'last_name': 'Last',
            'birth_date': '2002-12-20',
            'course_id': self.env.ref('viseducat_core.vm_course_5').id,
            'batch_id': self.env.ref('viseducat_core.vm_batch_4').id,
            'phone': 32234234,
            'mobile': 93432,
            'email': 'nisak.ahir@gmail.com',
            'state': 'submit',
            'gender': 'm',
            'register_id': self.env.ref(
                'viseducat_admission.vm_admission_register_3').id,
            'student_id': self.env.ref('viseducat_core.vm_student_18').id,
            'fees_term_id': 2,
            'fees': 1000,
        }

        studnet_2 = self.vm_admission.create(vals_2)
        studnet_2.enroll_student()
        studnet_2.onchange_student()

        for admission in admissions:
            admission._onchange_name()
            admission.onchange_register()
            admission.onchange_course()
            admission._check_admission_register()
            admission._check_birthdate()
            admission.submit_form()
            admission.admission_confirm()
            admission.confirm_in_progress()
            admission.get_student_vals()
            admission.confirm_rejected()
            admission.confirm_pending()
            admission.confirm_cancel()
            admission.confirm_to_draft()
            admission.vis_student()


class TestAdmissionregister(TestAdmissionCommon):

    def setUp(self):
        super(TestAdmissionregister, self).setUp()

    def test_case_1_register(self):
        register = self.vm_register.search([])

        for registers in register:
            logging.info('Admission registar Name : %s :' % (registers.name))

        register.confirm_register()
        register.set_to_draft()
        register.cancel_register()
        register.start_application()
        register.start_admission()
        register.close_register()
        register.check_dates()
        register.check_no_of_admission()


class TestAdmissionAnalysisWizard(TestAdmissionCommon):

    def setUp(self):
        super(TestAdmissionAnalysisWizard, self).setUp()

    def test_wizard_admission_analysis(self):
        vals = {
            'course_id': self.env.ref('viseducat_core.vm_course_2').id,
            'start_date': '2018-01-01',
            'end_date': '2019-12-30',
        }
        admission = self.wizard_admission.create(vals)
        admission.print_report()
