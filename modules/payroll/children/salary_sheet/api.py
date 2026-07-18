"""API endpoints for payroll.salary_sheet (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_salary_sheet_api
    register_salary_sheet_api(bp)
"""
from flask import jsonify


def register_salary_sheet_api(bp):
    @bp.route("/api/salary_sheet", endpoint="salary_sheet_api_list")
    def _salary_sheet_api_list():
        return jsonify(data=[], module="payroll", child="salary_sheet")
