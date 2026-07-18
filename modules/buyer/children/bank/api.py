"""API endpoints for buyer.bank (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_bank_api
    register_bank_api(bp)
"""
from flask import jsonify


def register_bank_api(bp):
    @bp.route("/api/bank", endpoint="bank_api_list")
    def _bank_api_list():
        return jsonify(data=[], module="buyer", child="bank")
