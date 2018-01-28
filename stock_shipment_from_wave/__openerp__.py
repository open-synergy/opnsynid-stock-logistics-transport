# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Create Shipment Plan From Picking Wave",
    "summary": "Create Shipment Plan From Picking Wave",
    "version": "8.0.1.0.0",
    "category": "Stock Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "stock_shipment_management",
        "stock_picking_wave_management",
    ],
    "data": [
        "views/stock_picking_wave_views.xml",
    ],
}
