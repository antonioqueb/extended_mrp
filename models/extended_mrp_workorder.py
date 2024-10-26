# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExtendedMrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    stage_id = fields.Many2one('mrp.production.stage', related='production_id.stage_id', store=True)
    stage_specific_data = fields.Text(string='Stage Specific Data')

    @api.model
    def create(self, vals):
        workorder = super(ExtendedMrpWorkorder, self).create(vals)
        if workorder.production_id and workorder.production_id.stage_id:
            workorder.workcenter_id = workorder.production_id.stage_id.workcenter_id
        return workorder

    def button_start(self):
        res = super(ExtendedMrpWorkorder, self).button_start()
        if self.stage_id.name in ['Lamination', 'Rehandling']:
            return self.env['quick.change.wizard'].create({
                'workorder_id': self.id,
            }).action_quick_change()
        return res