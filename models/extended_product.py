# -*- coding: utf-8 -*-
# models/extended_product.py
from odoo import models, fields, api

class ExtendedProductTemplate(models.Model):
    _inherit = 'product.template'

    is_intermediate = fields.Boolean(string='Es Producto Intermedio')
    stage_specifications = fields.Text(string='Especificaciones de Etapa')

class ExtendedProductProduct(models.Model):
    _inherit = 'product.product'

    @api.depends('bom_ids', 'bom_ids.stage_id')
    def _compute_bom_price(self, bom, boms_to_recompute=False):
        price = super(ExtendedProductProduct, self)._compute_bom_price(bom, boms_to_recompute)
        if bom.stage_id:
            # Agregar lógica de cálculo de costo específico de la etapa aquí
            stage_cost = 0  # Reemplazar con el cálculo real
            price += stage_cost
        return price