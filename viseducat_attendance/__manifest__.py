# -*- coding: utf-8 -*-
{
    'name': "viseducat_attendance",

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
    'depends': ['base','mail','viseducat_timetable'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/vm_security.xml',
        'views/attendance_register_view.xml',
        'views/attendance_line_view.xml',
        'views/attendance_sheet_view.xml',
        'views/attendance_type_view.xml',
        'views/attendance_session_view.xml',
        'data/attendance_sheet_sequence.xml',
        'menus/vm_menu.xml',
        'wizards/attendance_import_view.xml',
        'wizards/student_attendance_wizard_view.xml',
        'report/report_menu.xml',
        'report/student_attendance_report.xml',




    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/attendance_register_demo.xml',
        # 'demo/attendance_sheet_demo.xml',
        # 'demo/attendance_line_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
