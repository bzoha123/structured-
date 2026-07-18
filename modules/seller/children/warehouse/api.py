"""API endpoints for seller.warehouse (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_warehouse_api
    register_warehouse_api(bp)
"""
from flask import jsonify


def register_warehouse_api(bp):
    @bp.route("/api/warehouse", endpoint="warehouse_api_list")
    def _warehouse_api_list():
        return jsonify(data=[], module="seller", child="warehouse")
