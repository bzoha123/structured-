"""API endpoints for sales.goods_delivery_note (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_goods_delivery_note_api
    register_goods_delivery_note_api(bp)
"""
from flask import jsonify


def register_goods_delivery_note_api(bp):
    @bp.route("/api/goods_delivery_note", endpoint="goods_delivery_note_api_list")
    def _goods_delivery_note_api_list():
        return jsonify(data=[], module="sales", child="goods_delivery_note")
