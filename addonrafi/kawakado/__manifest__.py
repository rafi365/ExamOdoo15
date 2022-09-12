# -*- coding: utf-8 -*-
{
    'name': "kawakado",

    'summary': """
        KAWAKADO Corp ERP Software""",

    'description': """
        An ERP Software for KAWAKADO Corp for HashMicro Training Exam
    """,

    'author': "KAWAKADO Corp",
    'website': "https://www.hashmicro.com/id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/voiceactor_view.xml',
        'views/character_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
