# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QuickChangeWizard(models.TransientModel):
    _name = 'quick.change.wizard'
    _description = 'Quick Change Wizard'

    workorder_id = fields.Many2one('mrp.workorder', string='Work Order')
    new_product_id = fields.Many2one('product.product', string='New Product')

    def action_quick_change(self):
        self.ensure_one()
        if self.new_product_id:
            self.workorder_id.production_id.write({
                'product_id': self.new_product_id.id,
                'product_uom_id': self.new_product_id.uom_id.id,
            })
            # Additional logic for quick change
        return {'type': 'ir.actions.act_window_close'}