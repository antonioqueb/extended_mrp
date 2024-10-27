# File: models/mrp_production_stage.py

from odoo import models, fields, api

class MrpProductionStage(models.Model):
    _name = 'mrp.production.stage'
    _description = 'Etapa de Producción'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre de Etapa', required=True)
    sequence = fields.Integer(string='Secuencia', default=10)
    code = fields.Char(string='Código de Etapa', required=True)
    workcenter_ids = fields.Many2many('mrp.workcenter', string='Centros de Trabajo')
    required_data_ids = fields.Many2many('mrp.stage.data.field', string='Campos de Datos Requeridos')
    next_stage_id = fields.Many2one('mrp.production.stage', string='Siguiente Etapa')

    @api.model
    def create(self, vals):
        if 'sequence' not in vals:
            vals['sequence'] = self.search([], order='sequence desc', limit=1).sequence + 1
        return super(MrpProductionStage, self).create(vals)

class MrpStageDataField(models.Model):
    _name = 'mrp.stage.data.field'
    _description = 'Campo de Datos de Etapa'

    name = fields.Char(string='Nombre del Campo', required=True)
    field_type = fields.Selection([
        ('char', 'Texto'),
        ('integer', 'Entero'),
        ('float', 'Decimal'),
        ('boolean', 'Booleano'),
        ('date', 'Fecha'),
        ('datetime', 'Fecha y Hora')
    ], string='Tipo de Campo', required=True)
    is_required = fields.Boolean(string='Requerido')
    stage_id = fields.Many2one('mrp.production.stage', string='Etapa')