# -*- coding: utf-8 -*-

from odoo import tools
from odoo import api, fields, models

class ExtendedMrpProductionReport(models.Model):
    _name = 'report.extended_mrp_production'
    _description = 'Extended MRP Production Report'
    _auto = False

    production_id = fields.Many2one('mrp.production', string='Manufacturing Order', readonly=True)
    stage_id = fields.Many2one('mrp.production.stage', string='Production Stage', readonly=True)
    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    quantity = fields.Float(string='Quantity', readonly=True)
    date_planned_start = fields.Datetime(string='Planned Start Date', readonly=True)
    date_planned_finished = fields.Datetime(string='Planned End Date', readonly=True)
    octagon_runs = fields.Integer(string='Octagon Runs', readonly=True)
    cuts_per_shift = fields.Integer(string='Cuts per Shift', readonly=True)
    glued_reticles = fields.Integer(string='Glued Reticles', readonly=True)
    linear_meters = fields.Float(string='Linear Meters', readonly=True)
    finished_pallets = fields.Integer(string='Finished Pallets', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(f"""
            CREATE or REPLACE VIEW {self._table} as (
                SELECT
                    p.id as id,
                    p.id as production_id,
                    p.stage_id as stage_id,
                    p.product_id as product_id,
                    p.product_qty as quantity,
                    p.date_planned_start_wo as date_planned_start,
                    p.date_planned_finished_wo as date_planned_finished,
                    p.octagon_runs as octagon_runs,
                    p.cuts_per_shift as cuts_per_shift,
                    p.glued_reticles as glued_reticles,
                    p.linear_meters as linear_meters,
                    p.finished_pallets as finished_pallets
                FROM mrp_production p
            )
        """)