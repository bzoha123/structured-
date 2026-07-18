"""API endpoints for chart_of_accounts.level4 (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_level4_api
    register_level4_api(bp)
"""
from flask import jsonify


def register_level4_api(bp):
    @bp.route("/api/level4", endpoint="level4_api_list")
    def _level4_api_list():
        return jsonify(data=[], module="chart_of_accounts", child="level4")
