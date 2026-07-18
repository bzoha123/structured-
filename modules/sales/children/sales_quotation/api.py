"""API endpoints for sales.sales_quotation (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_quotation_api
    register_sales_quotation_api(bp)
"""
from flask import jsonify


def register_sales_quotation_api(bp):
    @bp.route("/api/sales_quotation", endpoint="sales_quotation_api_list")
    def _sales_quotation_api_list():
        return jsonify(data=[], module="sales", child="sales_quotation")
