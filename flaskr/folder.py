"""
文件夹：查看文件夹
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('folder', __name__, url_prefix='/folder')
cors = CORS(bp)


# 传入（账号 页码 每一页文件夹数） 返回 （账号所拥有的文件夹）
@bp.route('/display', methods='GET')
def display():
    username = request.args.get("username")
    page = request.args.get('page')
    number = request.args.get('number')
    row_count = page * number  # appear_page
    offset = (page - 1) * number  # ?? current_page

    db = get_db()
    user_id = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    folders = db.execute(
        'SELECT * FROM folder WHERE author_id = ? OFFSET ? ', (username, offset)
    ).fetchmany(row_count)
    # ...
    return jsonify({"msg": 1})
