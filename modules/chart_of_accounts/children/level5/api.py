"""API endpoints for chart_of_accounts.level5 (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_level5_api
    register_level5_api(bp)
"""
from flask import jsonify


def register_level5_api(bp):
    @bp.route("/api/level5", endpoint="level5_api_list")
    def _level5_api_list():
        return jsonify(data=[], module="chart_of_accounts", child="level5")
