"""API endpoints for sales.goods_return_request (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_goods_return_request_api
    register_goods_return_request_api(bp)
"""
from flask import jsonify


def register_goods_return_request_api(bp):
    @bp.route("/api/goods_return_request", endpoint="goods_return_request_api_list")
    def _goods_return_request_api_list():
        return jsonify(data=[], module="sales", child="goods_return_request")
