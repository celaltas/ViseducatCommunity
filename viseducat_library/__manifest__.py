# -*- coding: utf-8 -*-
{
    'name': "viseducat_library",

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
    'depends': ['account', 'base_automation', 'viseducat_activity', 'viseducat_parent'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'menus/vm_menu.xml',
        'data/media_queue_sequence.xml',
        'data/product_demo.xml',
        'views/publisher_view.xml',
        'views/library_view.xml',
        'views/author_view.xml',
        'views/media_type.xml',
        'views/tag_view.xml',
        'views/media_view.xml',
        'views/media_unit_view.xml',
        'views/media_movement_view.xml',
        'views/media_queue_view.xml',
        'views/media_purchase_view.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
        'wizards/return_media_view.xml',
        'wizards/issue_media_view.xml',
        'report/report_menu.xml',
        'report/report_library_card_barcode.xml',
        'report/report_media_barcode.xml',
        'report/report_student_library_card.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
