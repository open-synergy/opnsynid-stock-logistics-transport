# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import itertools
from openerp import models, api


class StockPickingWave(models.Model):
    _inherit = "stock.picking.wave"

    @api.multi
    def action_create_shipment_plans(self):
        for wave in self:
            wave._create_shipment_plans()

    @api.multi
    def _create_shipment_plans(self):
        self.ensure_one()
        obj_wiz = self.env["shipment.plan.creator"]
        moves = self.pickings_products.\
            filtered(lambda r: r.state not in ["done", "cancel"] and
                     r.location_dest_id.usage == "transit" and
                     not r.departure_shipment_id)
        origin_address = set(moves.mapped("ship_from_address_id"))
        destination_address = set(moves.mapped("ship_to_address_id"))
        for plan_combination in itertools.product(
                origin_address, destination_address):
            combine_moves = \
                moves.filtered(
                    lambda r: r.ship_from_address_id ==
                    plan_combination[0] and
                    r.ship_to_address_id == plan_combination[1])
            context = {
                "active_model": "stock.move",
                "active_ids": combine_moves.ids,
            }
            wiz = obj_wiz.with_context(context).create({})
            criteria = [
                ("wave", "=", self.id),
                ("state", "not in", ["done", "cancel"]),
                ("ship_from_address_id", "=", plan_combination[0].id),
                ("ship_to_address_id", "=", plan_combination[1].id),
                ("departure_shipment_id.state", "=", "draft"),
            ]
            similar_moves = self.env["stock.move"].search(criteria, limit=1)
            if len(similar_moves) == 1:
                wiz.write({"shipment_id": similar_moves[
                          0].departure_shipment_id.id})
            wiz.action_create_shipment()
