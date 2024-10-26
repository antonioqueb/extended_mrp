# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ExtendedMrpProduction(models.Model):
    _inherit = 'mrp.production'

    stage_id = fields.Many2one('mrp.production.stage', string='Production Stage')
    octagon_runs = fields.Integer(string='Octagon Runs')
    cuts_per_shift = fields.Integer(string='Cuts per Shift')
    glued_reticles = fields.Integer(string='Glued Reticles')
    linear_meters = fields.Float(string='Linear Meters')
    finished_pallets = fields.Integer(string='Finished Pallets')

    @api.model
    def create(self, vals):
        if 'stage_id' not in vals:
            first_stage = self.env['mrp.production.stage'].search([], order='sequence', limit=1)
            if first_stage:
                vals['stage_id'] = first_stage.id
        return super(ExtendedMrpProduction, self).create(vals)

    def action_confirm(self):
        for production in self:
            if not production.stage_id:
                raise UserError(_("Please set a production stage before confirming."))
        return super(ExtendedMrpProduction, self).action_confirm()

    def action_next_stage(self):
        for production in self:
            next_stage = self.env['mrp.production.stage'].search([
                ('sequence', '>', production.stage_id.sequence)
            ], order='sequence', limit=1)
            if next_stage:
                production.write({'stage_id': next_stage.id})
            else:
                raise UserError(_("This is the final stage of production."))

    def _generate_moves(self):
        moves = super(ExtendedMrpProduction, self)._generate_moves()
        for move in moves:
            move.production_stage_id = self.stage_id.id
        return moves