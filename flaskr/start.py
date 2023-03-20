"""
Start：新建笔记、上传音频、查看用户笔记、文件夹
Pending: create(),upload()
"""
import random
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('start', __name__, url_prefix='/start')
cors = CORS(bp)


# 新建笔记
@bp.route('/create', methods=['GET', ])
def create():
    """
    omitted
    """
    return jsonify({"msg": 1})


# 上传音频并新建笔记
@bp.route('/upload', methods=['GET', ])
def upload():
    """
    omitted
    """
    user_id = session.get('user_id')
    foldername = 'default'
    content = "padding"  # 笔记内容待补充

    db = get_db()
    folder = db.execute(
        'SELECT * FROM folder WHERE author_id = ? and foldername = ?', (user_id, foldername)
    )
    db.execute(
        'INSERT INTO document (author_id, folder_id, content) VALUES (?, ?)', (user_id, folder['id'], content)
    )
    db.commit()

    return jsonify({"msg": 1})


# 笔记 传入 （账号 current_page 页码 每一页文件数） 返回 （账号所拥有的笔记）
@bp.route('/display', methods=['GET', ])
def display():
    username = request.args.get("username")
    # page = request.args.get('page')
    number = request.args.get('number')
    offset = request.args.get('current_page')

    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()
    doc = db.execute(
        'SELECT * FROM document WHERE author_id = ? OFFSET ? ', (user['id'], offset)
    ).fetchmany(number)

    # docs [[id,author_id,folder_id,content,created],[],...]
    docs = [list(item) for item in doc]

    return jsonify({"docs": docs})


# 文件夹 传入 （账号） 返回 （状态） 后端（随机给文件夹生成名字）
@bp.route('/directory', methods=['GET', ])
def directory():
    username = request.args.get("username")
    foldername = 'folder_' + random.randint(1, 100)

    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()
    db.execute('INSERT INTO folder (author_id, foldername) VALUES (?, ?)', (user['id'], foldername))
    db.commit()

    return jsonify({"msg": 1})
