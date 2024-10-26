# -*- coding: utf-8 -*-

from odoo import models, fields

class ExtendedQualityCheck(models.Model):
    _inherit = 'quality.check'

    production_stage_id = fields.Many2one('mrp.production.stage', string='Production Stage')
    stage_specific_data = fields.Text(string='Stage Specific Data')