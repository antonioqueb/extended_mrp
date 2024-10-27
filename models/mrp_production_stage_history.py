# file: models/mrp_production_stage_history.py

from odoo import models, fields

class MrpProductionStageHistory(models.Model):
    _name = 'mrp.production.stage.history'
    _description = 'Historial de Etapas de Producción'
    _order = 'create_date desc'

    production_id = fields.Many2one('mrp.production', string='Orden de Producción', required=True)
    stage_id = fields.Many2one('mrp.production.stage', string='Etapa', required=True)
    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    create_date = fields.Datetime(string='Fecha de Cambio', readonly=True)