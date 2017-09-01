# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    notify_party_id = fields.Many2one(
        string="Notify Party",
        comodel_name="res.partner",
    )
