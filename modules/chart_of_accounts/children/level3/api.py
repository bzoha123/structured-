"""API endpoints for chart_of_accounts.level3 (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_level3_api
    register_level3_api(bp)
"""
from flask import jsonify


def register_level3_api(bp):
    @bp.route("/api/level3", endpoint="level3_api_list")
    def _level3_api_list():
        return jsonify(data=[], module="chart_of_accounts", child="level3")
