"""API endpoints for purchase.goods_receipt_note (JSON).

Generated stub. Register on the area blueprint in routes.py, e.g.:
    from .api import register_goods_receipt_note_api
    register_goods_receipt_note_api(bp)
"""
from flask import jsonify


def register_goods_receipt_note_api(bp):
    @bp.route("/api/goods_receipt_note", endpoint="goods_receipt_note_api_list")
    def _goods_receipt_note_api_list():
        return jsonify(data=[], module="purchase", child="goods_receipt_note")
