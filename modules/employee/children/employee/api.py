"""API endpoints for employee.employee (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_employee_api
    register_employee_api(bp)
"""
from flask import jsonify


def register_employee_api(bp):
    @bp.route("/api/employee", endpoint="employee_api_list")
    def _employee_api_list():
        return jsonify(data=[], module="employee", child="employee")
