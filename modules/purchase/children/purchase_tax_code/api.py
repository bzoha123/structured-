"""API endpoints for purchase.purchase_tax_code (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_purchase_tax_code_api
    register_purchase_tax_code_api(bp)
"""
from flask import jsonify


def register_purchase_tax_code_api(bp):
    @bp.route("/api/purchase_tax_code", endpoint="purchase_tax_code_api_list")
    def _purchase_tax_code_api_list():
        return jsonify(data=[], module="purchase", child="purchase_tax_code")
