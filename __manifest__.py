# -*- coding: utf-8 -*-
{
    'name': 'Extended MRP',
    'version': '1.0',
    'summary': 'Extiende la funcionalidad MRP para producción multi-etapa',
    'description': """
        Este módulo extiende la funcionalidad MRP en Odoo 17 para manejar un 
        proceso de producción multi-etapa incluyendo Octágono, Corte, Pegado, 
        Laminado y Remanejo.
    """,
    'category': 'Manufacturing',
    'author': 'Tu Empresa',
    'website': 'https://www.tuempresa.com',
    'depends': ['mrp', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/extended_mrp_views.xml',
        'views/production_stage_views.xml',
        'views/product_views.xml',
        'reports/extended_mrp_report_views.xml',
        'wizards/quick_change_wizard_view.xml',
        'data/production_stage_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}