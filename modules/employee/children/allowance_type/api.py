"""API endpoints for employee.allowance_type (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_allowance_type_api
    register_allowance_type_api(bp)
"""
from flask import jsonify


def register_allowance_type_api(bp):
    @bp.route("/api/allowance_type", endpoint="allowance_type_api_list")
    def _allowance_type_api_list():
        return jsonify(data=[], module="employee", child="allowance_type")
