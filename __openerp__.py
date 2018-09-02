# -*- coding: utf-8 -*-
{
    'name': "Chasqui",

    'summary': """
        Este modulo hace obligatorios los campos segun el dominio, para ser usado en 
        con el adaptador odoo-chasqui.""",

    'description': """
        Este modulo hace obligatorios los campos segun el dominio, para ser usado en 
        con el adaptador odoo-chasqui.
    """,

    'author': "Fernando J. Recci - Geneos",
    'website': "http://www.geneos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}