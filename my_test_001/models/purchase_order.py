# Copyright 2022 Ratty123
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"
