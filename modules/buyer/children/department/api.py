"""API endpoints for buyer.department (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_department_api
    register_department_api(bp)
"""
from flask import jsonify


def register_department_api(bp):
    @bp.route("/api/department", endpoint="department_api_list")
    def _department_api_list():
        return jsonify(data=[], module="buyer", child="department")
