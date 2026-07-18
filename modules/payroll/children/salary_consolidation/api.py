"""API endpoints for payroll.salary_consolidation (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_salary_consolidation_api
    register_salary_consolidation_api(bp)
"""
from flask import jsonify


def register_salary_consolidation_api(bp):
    @bp.route("/api/salary_consolidation", endpoint="salary_consolidation_api_list")
    def _salary_consolidation_api_list():
        return jsonify(data=[], module="payroll", child="salary_consolidation")
