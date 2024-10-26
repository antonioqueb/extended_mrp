# -*- coding: utf-8 -*-

from odoo import models, fields

class MrpProductionStage(models.Model):
    _name = 'mrp.production.stage'
    _description = 'Etapa de Producción'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre de la Etapa', required=True)
    sequence = fields.Integer(string='Secuencia', default=10)
    workcenter_id = fields.Many2one('mrp.workcenter', string='Centro de Trabajo')
    description = fields.Text(string='Descripción')
    is_intermediate_stock = fields.Boolean(string='Tiene Stock Intermedio')