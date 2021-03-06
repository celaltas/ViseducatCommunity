# -*- coding: utf-8 -*-
{
    'name': "viseducat_timetable",

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
    'depends': ['base', 'mail', 'viseducat_classroom'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'views/timetable_view.xml',
        'views/timetable_templates.xml',
        'views/timing_view.xml',
        'views/faculty_view.xml',
        'menus/vm_menu.xml',
        'wizard/generate_timetable_view.xml',
        'wizard/time_table_report.xml',
        'report/report_menu.xml',
        'report/report_timetable_student_generate.xml',
        'report/report_timetable_teacher_generate.xml',

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
