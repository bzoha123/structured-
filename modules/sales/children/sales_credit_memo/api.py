"""API endpoints for sales.sales_credit_memo (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_sales_credit_memo_api
    register_sales_credit_memo_api(bp)
"""
from flask import jsonify


def register_sales_credit_memo_api(bp):
    @bp.route("/api/sales_credit_memo", endpoint="sales_credit_memo_api_list")
    def _sales_credit_memo_api_list():
        return jsonify(data=[], module="sales", child="sales_credit_memo")
