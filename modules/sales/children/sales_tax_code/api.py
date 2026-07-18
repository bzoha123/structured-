"""API endpoints for sales.sales_tax_code (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_tax_code_api
    register_sales_tax_code_api(bp)
"""
from flask import jsonify


def register_sales_tax_code_api(bp):
    @bp.route("/api/sales_tax_code", endpoint="sales_tax_code_api_list")
    def _sales_tax_code_api_list():
        return jsonify(data=[], module="sales", child="sales_tax_code")
