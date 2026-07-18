"""API endpoints for vendor.documents (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_documents_api
    register_documents_api(bp)
"""
from flask import jsonify


def register_documents_api(bp):
    @bp.route("/api/documents", endpoint="documents_api_list")
    def _documents_api_list():
        return jsonify(data=[], module="vendor", child="documents")
