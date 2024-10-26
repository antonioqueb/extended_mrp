# -*- coding: utf-8 -*-

from odoo import models, fields

class ExtendedMrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    stage_capacity = fields.Float(string='Stage Capacity')
    stage_efficiency = fields.Float(string='Stage Efficiency')