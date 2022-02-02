# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProcurementGroup(models.Model):
    _inherit = "procurement.group"

    notify_party_id = fields.Many2one(
        string="Notify Party",
        comodel_name="res.partner",
    )
