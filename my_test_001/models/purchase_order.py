# Copyright 2022 Ratty123
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"
    x_purchase_line_count = fields.Char(
        string='Test Text', compute="_compute_line_count", store=True)

    @api.depends('order_line')
    def _compute_line_count(self):
        for order in self:
            order.x_purchase_line_count = len(order.order_line)
