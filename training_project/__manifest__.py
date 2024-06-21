# -*- coding: utf-8 -*-
{
    'name': "Training Project",

    'summary': """
            PDC Customizations
        """,

    'description': """

    """,

    'author': "Akarigo",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',
    "application": True,
    # any module necessary for this one to work correctly

    'depends': ['base', 'sale'],

    # always loaded
    'data': ['views/sale_order_view.xml'],
    'assets': {
        'web.assets_backend': [
            '/pdc/static/src/js/variant_mixin_pricelist.js',
            '/pdc/static/src/js/product_configurator.js',
        ],
    },
}
