"""API endpoints for employee.allowance (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_allowance_api
    register_allowance_api(bp)
"""
from flask import jsonify


def register_allowance_api(bp):
    @bp.route("/api/allowance", endpoint="allowance_api_list")
    def _allowance_api_list():
        return jsonify(data=[], module="employee", child="allowance")
