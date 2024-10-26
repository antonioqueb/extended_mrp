# -*- coding: utf-8 -*-

from odoo import models, fields

class ExtendedQualityCheck(models.Model):
    _name = 'extended.quality.check'
    _description = 'Extended Quality Check'

    name = fields.Char(string='Name', required=True)
    production_stage_id = fields.Many2one('mrp.production.stage', string='Production Stage')
    stage_specific_data = fields.Text(string='Stage Specific Data')
    # Add other fields as needed