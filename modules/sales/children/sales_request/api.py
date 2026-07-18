"""API endpoints for sales.sales_request (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_request_api
    register_sales_request_api(bp)
"""
from flask import jsonify


def register_sales_request_api(bp):
    @bp.route("/api/sales_request", endpoint="sales_request_api_list")
    def _sales_request_api_list():
        return jsonify(data=[], module="sales", child="sales_request")
