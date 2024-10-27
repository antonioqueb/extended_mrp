# File: models/mrp_production_stage_data.py
# models/mrp_production_stage_data.py
from odoo import models, fields, api

class MrpProductionStageData(models.Model):
    _name = 'mrp.production.stage.data'
    _description = 'Datos de Etapa de Producción'

    production_id = fields.Many2one('mrp.production', string='Orden de Producción', required=True)
    stage_id = fields.Many2one('mrp.production.stage', string='Etapa', required=True)
    field_id = fields.Many2one('mrp.stage.data.field', string='Campo de Datos', required=True)
    field_type = fields.Selection(related='field_id.field_type', string='Tipo de Campo', readonly=True)
    value_char = fields.Char(string='Valor de Texto')
    value_integer = fields.Integer(string='Valor Entero')
    value_float = fields.Float(string='Valor Decimal')
    value_boolean = fields.Boolean(string='Valor Booleano')
    value_date = fields.Date(string='Valor de Fecha')
    value_datetime = fields.Datetime(string='Valor de Fecha y Hora')

    @api.depends('field_type', 'value_char', 'value_integer', 'value_float', 'value_boolean', 'value_date', 'value_datetime')
    def _compute_value(self):
        for record in self:
            if record.field_type == 'char':
                record.value = record.value_char
            elif record.field_type == 'integer':
                record.value = record.value_integer
            elif record.field_type == 'float':
                record.value = record.value_float
            elif record.field_type == 'boolean':
                record.value = record.value_boolean
            elif record.field_type == 'date':
                record.value = record.value_date
            elif record.field_type == 'datetime':
                record.value = record.value_datetime
            else:
                record.value = False

    value = fields.Char(string='Valor', compute='_compute_value', store=True)

    @api.onchange('field_id')
    def _onchange_field_id(self):
        self.value_char = False
        self.value_integer = False
        self.value_float = False
        self.value_boolean = False
        self.value_date = False
        self.value_datetime = False

    def name_get(self):
        return [(record.id, f"{record.production_id.name} - {record.stage_id.name} - {record.field_id.name}") for record in self]