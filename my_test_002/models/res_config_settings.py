# Copyright 2022 Ratty123
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    my_test_bool_field = fields.Boolean(
        related="company_id.my_test_bool_field",
        readonly=False
    )
    my_test_chars_field = fields.Char(
        related="company_id.my_test_chars_field",
        readonly=False
    )
