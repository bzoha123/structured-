"""API endpoints for buyer.buyer (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_buyer_api
    register_buyer_api(bp)
"""
from flask import jsonify


def register_buyer_api(bp):
    @bp.route("/api/buyer", endpoint="buyer_api_list")
    def _buyer_api_list():
        return jsonify(data=[], module="buyer", child="buyer")
