"""API endpoints for payroll.payroll_process (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_payroll_process_api
    register_payroll_process_api(bp)
"""
from flask import jsonify


def register_payroll_process_api(bp):
    @bp.route("/api/payroll_process", endpoint="payroll_process_api_list")
    def _payroll_process_api_list():
        return jsonify(data=[], module="payroll", child="payroll_process")
