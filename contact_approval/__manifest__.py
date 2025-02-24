# -*- coding: utf-8 -*-
{
    'name': "contact_approval",

    'summary': "Project training Contact Approval",

    'description': """
Project training Contact Approval
    """,

    'author': "Pikopik",
    'website': "training-contact.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/contact_approval_view.xml',
        'views/contact_approval_menu.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

