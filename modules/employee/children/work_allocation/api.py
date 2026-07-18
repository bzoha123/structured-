"""API endpoints for employee.work_allocation (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_work_allocation_api
    register_work_allocation_api(bp)
"""
from flask import jsonify


def register_work_allocation_api(bp):
    @bp.route("/api/work_allocation", endpoint="work_allocation_api_list")
    def _work_allocation_api_list():
        return jsonify(data=[], module="employee", child="work_allocation")
