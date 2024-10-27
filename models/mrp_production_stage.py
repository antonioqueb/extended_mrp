# File: models/mrp_production_stage.py

from odoo import models, fields, api

class MrpProductionStage(models.Model):
    _name = 'mrp.production.stage'
    _description = 'Etapa de Producción'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre de Etapa', required=True)
    sequence = fields.Integer(string='Secuencia', default=10)
    code = fields.Char(string='Código de Etapa', required=True)
    workcenter_id = fields.Many2one('mrp.workcenter', string='Centro de Trabajo')  # Changed from Many2many to Many2one
    required_data_ids = fields.Many2many('mrp.stage.data.field', string='Campos de Datos Requeridos')
    next_stage_id = fields.Many2one('mrp.production.stage', string='Siguiente Etapa')
    is_intermediate_stock = fields.Boolean(string='Es Stock Intermedio', default=False)

    @api.model
    def create(self, vals):
        if 'sequence' not in vals:
            vals['sequence'] = self.search([], order='sequence desc', limit=1).sequence + 1
        return super(MrpProductionStage, self).create(vals)

# ... rest of the file remains the same