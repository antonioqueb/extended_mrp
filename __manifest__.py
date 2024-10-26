# -*- coding: utf-8 -*-
{
    'name': 'Extended MRP',
    'version': '1.0',
    'summary': 'Extends MRP functionality for multi-stage production',
    'description': """
        This module extends the MRP functionality in Odoo 17 to handle a 
        multi-stage production process including Octagon, Cutting, Gluing, 
        Lamination, and Rehandling stages.
    """,
    'category': 'Manufacturing',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['mrp', 'stock', 'quality'],
    'data': [
        'security/ir.model.access.csv',
        'views/extended_mrp_views.xml',
        'views/production_stage_views.xml',
        'views/product_views.xml',
        'views/quality_views.xml',
        'reports/extended_mrp_report_views.xml',
        'wizards/quick_change_wizard_view.xml',
        'data/production_stage_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}