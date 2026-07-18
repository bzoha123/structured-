"""API endpoints for chart_of_accounts.level2 (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_level2_api
    register_level2_api(bp)
"""
from flask import jsonify


def register_level2_api(bp):
    @bp.route("/api/level2", endpoint="level2_api_list")
    def _level2_api_list():
        return jsonify(data=[], module="chart_of_accounts", child="level2")
