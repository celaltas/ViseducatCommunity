# -*- coding: utf-8 -*-
{
    'name': "Viseducat Core",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'hr', 'web', 'website'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'report/report_menu.xml',
        'report/report_student_bonafide.xml',
        'report/report_student_idcard.xml',
        'wizard/faculty_create_employee_wizard_view.xml',
        'wizard/faculty_create_user_wizard_view.xml',
        'wizard/students_create_user_wizard_view.xml',
        'views/department_view.xml',
        'views/res_company_view.xml',
        'views/student_view.xml',
        'views/hr_view.xml',
        'views/category_view.xml',
        'views/course_view.xml',
        'views/batch_view.xml',
        'views/subject_view.xml',
        'views/faculty_view.xml',
        #'views/website_assets.xml',
        'views/subject_registration_view.xml',
        #'views/res_config_setting_view.xml',
        'views/student_portal_view.xml',
        'views/student_course_view.xml',
        # 'data/ir_cron_data.xml',
        'menu/viseducat_core_menu.xml',
        'menu/faculty_menu.xml',
        'menu/student_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/student_demo.xml',
        'demo/faculty_demo.xml',
        'demo/department_demo.xml',
        'demo/course_demo.xml',
        'demo/batch_demo.xml',
        'demo/subject_demo.xml',

    ],
}
