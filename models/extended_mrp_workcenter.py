# -*- coding: utf-8 -*-
# models/extended_mrp_workcenter.py
from odoo import models, fields

class ExtendedMrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    stage_capacity = fields.Float(string='Capacidad de la Etapa')
    stage_efficiency = fields.Float(string='Eficiencia de la Etapa')