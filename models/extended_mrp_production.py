# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ExtendedMrpProduction(models.Model):
    _inherit = 'mrp.production'

    stage_id = fields.Many2one('mrp.production.stage', string='Etapa de Producción', tracking=True)
    stage_history_ids = fields.One2many('mrp.production.stage.history', 'production_id', string='Historial de Etapas')
    octagon_runs = fields.Integer(string='Corridas de Octágono')
    cuts_per_shift = fields.Integer(string='Cortes por Turno')
    glued_reticles = fields.Integer(string='Retículas Pegadas')
    linear_meters = fields.Float(string='Metros Lineales')
    finished_pallets = fields.Integer(string='Tarimas Terminadas')

    @api.model
    def create(self, vals):
        if 'stage_id' not in vals:
            first_stage = self.env['mrp.production.stage'].search([('name', '=', 'Octágono')], limit=1)
            if first_stage:
                vals['stage_id'] = first_stage.id
            else:
                raise UserError(_("No se encontró la etapa 'Octágono'. Por favor, asegúrese de que está configurada."))
        
        production = super(ExtendedMrpProduction, self).create(vals)
        production._create_stage_history(production.stage_id.id)
        return production

    def write(self, vals):
        if 'stage_id' in vals:
            for production in self:
                production._create_stage_history(vals['stage_id'])
        return super(ExtendedMrpProduction, self).write(vals)

    def _create_stage_history(self, stage_id):
        self.ensure_one()
        self.env['mrp.production.stage.history'].create({
            'production_id': self.id,
            'stage_id': stage_id,
            'user_id': self.env.user.id,
        })

    def action_confirm(self):
        for production in self:
            if not production.stage_id:
                raise UserError(_("Por favor, establezca una etapa de producción antes de confirmar."))
        return super(ExtendedMrpProduction, self).action_confirm()

    def action_next_stage(self):
        for production in self:
            next_stage = self.env['mrp.production.stage'].search([
                ('sequence', '>', production.stage_id.sequence)
            ], order='sequence', limit=1)
            if next_stage:
                production.write({'stage_id': next_stage.id})
            else:
                raise UserError(_("Esta es la etapa final de producción."))

    def _generate_moves(self):
        moves = super(ExtendedMrpProduction, self)._generate_moves()
        for move in moves:
            move.production_stage_id = self.stage_id.id
        return moves