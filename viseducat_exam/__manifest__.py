# -*- coding: utf-8 -*-
{
    'name': "viseducat_exam",

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
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/vm_security.xml',
        'views/exam_view.xml',
        'views/exam_session_view.xml',
        'views/exam_attendees_view.xml',
        'views/result_template_view.xml',
        'views/marksheet_register_view.xml',
        'views/marksheet_line_view.xml',
        'views/result_line_view.xml',
        'views/exam_type_view.xml',
        'views/exam_room_view.xml',
        'views/grade_configuration_view.xml',
        'views/res_partner_view.xml',

        'report/report_ticket.xml',
        'report/student_marksheet.xml',
        'report/report_menu.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
