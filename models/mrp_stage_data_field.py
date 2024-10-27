# File: models/mrp_stage_data_field.py

from odoo import models, fields

class MrpStageDataField(models.Model):
    _name = 'mrp.stage.data.field'
    _description = 'Stage Data Field'

    name = fields.Char(string='Field Name', required=True)
    field_type = fields.Selection([
        ('char', 'Text'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('date', 'Date'),
        ('datetime', 'Date & Time')
    ], string='Field Type', required=True)
    is_required = fields.Boolean(string='Required')
    stage_id = fields.Many2one('mrp.production.stage', string='Stage')