"""API endpoints for purchase.purchase_request (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_request_api
    register_purchase_request_api(bp)
"""
from flask import jsonify


def register_purchase_request_api(bp):
    @bp.route("/api/purchase_request", endpoint="purchase_request_api_list")
    def _purchase_request_api_list():
        return jsonify(data=[], module="purchase", child="purchase_request")
