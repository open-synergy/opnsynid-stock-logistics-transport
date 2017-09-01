# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Order Notify Party",
    "version": "8.0.1.0.0",
    "category": "Stock Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "sale_transport_multi_address",
        "stock_transport_notify_party",
    ],
    "data": [
        "views/sale_order_views.xml",
    ],
}
