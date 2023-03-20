"""
Recent：查看笔记
Pending: 无
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('recent', __name__, url_prefix='/recent')
cors = CORS(bp)


# 传入（账号 current page 页码 每一页文件数） 返回 （账号所拥有的笔记）
@bp.route('/display', methods=['GET', ])
def display():
    username = request.args.get("username")
    # page = request.args.get('page')
    number = request.args.get('number')
    offset = request.args.get('current_page')

    db = get_db()
    user = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    doc = db.execute(
        'SELECT * FROM document WHERE author_id = ? OFFSET ? ', (user['id'], offset)
    ).fetchmany(number)

    # docs [[id,author_id,folder_id,content,created],[],...]
    docs = [list(item) for item in doc]

    return jsonify({"msg": 1, "docs": docs})
