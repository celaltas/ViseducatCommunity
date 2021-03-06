# -*- coding: utf-8 -*-
{
    'name': "viseducat_activity",

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
    'depends': ['viseducat_core'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'security/vm_security.xml',
         'menus/vm_menu.xml',
         'views/activity_view.xml',
         'views/activity_type_view.xml',
         'views/student_view.xml',
         'data/activity_type_data.xml',
         'wizard/student_migrate_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
