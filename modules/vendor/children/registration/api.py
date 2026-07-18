"""API endpoints for vendor.registration (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_registration_api
    register_registration_api(bp)
"""
from flask import jsonify


def register_registration_api(bp):
    @bp.route("/api/registration", endpoint="registration_api_list")
    def _registration_api_list():
        return jsonify(data=[], module="vendor", child="registration")
