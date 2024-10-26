# -*- coding: utf-8 -*-

from odoo import models, fields

class MrpProductionStage(models.Model):
    _name = 'mrp.production.stage'
    _description = 'Production Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    workcenter_id = fields.Many2one('mrp.workcenter', string='Work Center')
    description = fields.Text(string='Description')
    is_intermediate_stock = fields.Boolean(string='Has Intermediate Stock')