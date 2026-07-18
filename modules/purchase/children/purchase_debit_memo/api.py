"""API endpoints for purchase.purchase_debit_memo (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_debit_memo_api
    register_purchase_debit_memo_api(bp)
"""
from flask import jsonify


def register_purchase_debit_memo_api(bp):
    @bp.route("/api/purchase_debit_memo", endpoint="purchase_debit_memo_api_list")
    def _purchase_debit_memo_api_list():
        return jsonify(data=[], module="purchase", child="purchase_debit_memo")
