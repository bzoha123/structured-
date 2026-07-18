"""API endpoints for chart_of_accounts.level1 (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_level1_api
    register_level1_api(bp)
"""
from flask import jsonify


def register_level1_api(bp):
    @bp.route("/api/level1", endpoint="level1_api_list")
    def _level1_api_list():
        return jsonify(data=[], module="chart_of_accounts", child="level1")
