"""API endpoints for purchase.purchase_invoice (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_invoice_api
    register_purchase_invoice_api(bp)
"""
from flask import jsonify


def register_purchase_invoice_api(bp):
    @bp.route("/api/purchase_invoice", endpoint="purchase_invoice_api_list")
    def _purchase_invoice_api_list():
        return jsonify(data=[], module="purchase", child="purchase_invoice")
