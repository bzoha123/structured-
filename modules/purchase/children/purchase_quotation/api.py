"""API endpoints for purchase.purchase_quotation (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_quotation_api
    register_purchase_quotation_api(bp)
"""
from flask import jsonify


def register_purchase_quotation_api(bp):
    @bp.route("/api/purchase_quotation", endpoint="purchase_quotation_api_list")
    def _purchase_quotation_api_list():
        return jsonify(data=[], module="purchase", child="purchase_quotation")
