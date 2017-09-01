# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    notify_party_id = fields.Many2one(
        string="Notify Party",
        comodel_name="res.partner",
        states={
            "cancel": [
                ("readonly", True),
            ],
            "progress": [
                ("readonly", True),
            ],
            "manual": [
                ("readonly", True),
            ],
            "shipping_except": [
                ("readonly", True),
            ],
            "invoice_except": [
                ("readonly", True),
            ],
            "done": [
                ("readonly", True),
            ],
        },
    )

    @api.model
    def _prepare_procurement_group(self, order):
        _super = super(SaleOrder, self)
        res = _super._prepare_procurement_group(order)
        changes = {
            "notify_party_id": order.notify_party_id and
            order.notify_party_id.id or False,
        }
        res.update(changes)
        return res
