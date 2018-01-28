# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.multi
    def _picking_assign(self, procurement_group, location_from, location_to):
        _super = super(StockMove, self)
        res = _super._picking_assign(
            procurement_group, location_from, location_to)
        for picking in self.mapped("picking_id"):
            group = picking.group_id
            if not group:
                continue
            changes = {}
            if not picking.notify_party_id:
                changes["notify_party_id"] = group.notify_party_id and \
                    group.notify_party_id.id or False
            picking.write(changes)
        return res

    @api.model
    def _prepare_procurement_from_move(self, move):
        _super = super(StockMove, self)
        res = _super._prepare_procurement_from_move(move)
        update = {
            "notify_party_id": move.procurement_id.notify_party_id.id,
        }
        res.update(update)
        return res
