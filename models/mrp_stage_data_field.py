# File: models/mrp_stage_data_field.py

from odoo import models, fields

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