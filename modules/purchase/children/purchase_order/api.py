"""API endpoints for purchase.purchase_order (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_order_api
    register_purchase_order_api(bp)
"""
from flask import jsonify


def register_purchase_order_api(bp):
    @bp.route("/api/purchase_order", endpoint="purchase_order_api_list")
    def _purchase_order_api_list():
        return jsonify(data=[], module="purchase", child="purchase_order")
