# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    notify_party_id = fields.Many2one(
        related="group_id.notify_party_id",
        string="Notify Party",
        comodel_name="res.partner",
    )
