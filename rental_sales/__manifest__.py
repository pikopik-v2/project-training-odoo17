# -*- coding: utf-8 -*-
{
    'name': "rental_sales",

    'summary': "Aplikasi rental",

    'description': """
aplikasi rental sales
    """,

    'author': "Pikopik",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/rental_view.xml',
        'views/product_view.xml',
        'views/rental_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

