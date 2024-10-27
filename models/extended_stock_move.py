# -*- coding: utf-8 -*-
# models/extended_stock_move.py
from odoo import models, fields

class ExtendedStockMove(models.Model):
    _inherit = 'stock.move'

    production_stage_id = fields.Many2one('mrp.production.stage', string='Etapa de Producción')