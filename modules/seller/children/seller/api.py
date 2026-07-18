"""API endpoints for seller.seller (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_seller_api
    register_seller_api(bp)
"""
from flask import jsonify


def register_seller_api(bp):
    @bp.route("/api/seller", endpoint="seller_api_list")
    def _seller_api_list():
        return jsonify(data=[], module="seller", child="seller")
