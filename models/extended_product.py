# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExtendedProductTemplate(models.Model):
    _inherit = 'product.template'

    is_intermediate = fields.Boolean(string='Is Intermediate Product')
    stage_specifications = fields.Text(string='Stage Specifications')

class ExtendedProductProduct(models.Model):
    _inherit = 'product.product'

    @api.depends('bom_ids', 'bom_ids.stage_id')
    def _compute_bom_price(self, bom, boms_to_recompute=False):
        price = super(ExtendedProductProduct, self)._compute_bom_price(bom, boms_to_recompute)
        if bom.stage_id:
            # Add stage-specific cost calculation logic here
            stage_cost = 0  # Replace with actual calculation
            price += stage_cost
        return price