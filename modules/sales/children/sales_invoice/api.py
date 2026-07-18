"""API endpoints for sales.sales_invoice (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_invoice_api
    register_sales_invoice_api(bp)
"""
from flask import jsonify


def register_sales_invoice_api(bp):
    @bp.route("/api/sales_invoice", endpoint="sales_invoice_api_list")
    def _sales_invoice_api_list():
        return jsonify(data=[], module="sales", child="sales_invoice")
