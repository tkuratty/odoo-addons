# Copyright 2022 Ratty123
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    my_test_bool_field = fields.Boolean(
        string="Boolean Field",
        default=False,
        readonly=False
    )
    my_test_chars_field = fields.Char(
        string="Some text",
        default="default text",
        readonly=False
    )
