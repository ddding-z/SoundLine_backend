"""
Start：新建笔记、上传音频、查看用户笔记、文件夹
Pending: create(),upload(),display()
"""
import random
import markdown
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('start', __name__, url_prefix='/start')
cors = CORS(bp)


# 新建笔记 跳转至文件详情页面??
@bp.route('/create', methods='GET')
def create():
    return jsonify({"msg": 1})


# 上传音频、并新建笔记
@bp.route('/upload', methods='GET')
def upload():
    return jsonify({"msg": 1})


# 笔记 传入 （账号 current_page 页码 每一页文件数） 返回 （账号所拥有的笔记）
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
    docs = db.execute(
        'SELECT * FROM document WHERE author_id = ? OFFSET ? ', (user_id, offset)
    ).fetchmany(row_count)
    '''
    ToDo: 返回 （账号所拥有的笔记）
    '''
    return jsonify({"msg": 1})


# 文件夹 传入 （账号） 返回 （状态） 后端（随机给文件夹生成名字）
@bp.route('/directory', methods='GET')
def directory():
    username = request.args.get("username")
    name = 'folder_' + random.randint(1, 100)

    db = get_db()
    user_id = db.execute('SELECT id FROM user WHERE username = ?', (username,)
                         ).fetchone()
    db.execute('INSERT INTO folder (author_id, name) VALUES (?, ?)', (user_id, name))
    db.commit()

    return jsonify({"msg": 1})
