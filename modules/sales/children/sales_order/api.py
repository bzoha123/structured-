"""API endpoints for sales.sales_order (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_order_api
    register_sales_order_api(bp)
"""
from flask import jsonify


def register_sales_order_api(bp):
    @bp.route("/api/sales_order", endpoint="sales_order_api_list")
    def _sales_order_api_list():
        return jsonify(data=[], module="sales", child="sales_order")
