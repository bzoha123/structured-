"""API endpoints for payroll.reports (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_reports_api
    register_reports_api(bp)
"""
from flask import jsonify


def register_reports_api(bp):
    @bp.route("/api/reports", endpoint="reports_api_list")
    def _reports_api_list():
        return jsonify(data=[], module="payroll", child="reports")
