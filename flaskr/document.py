"""
文件详情页面：查看、修改、新建文件； chat
Pending: display(),create(),revise(),unfold()
"""

import markdown
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('document', __name__, url_prefix='/document')
cors = CORS(bp)


# 传入 （账号 文件id） 返回 （文件具体内容和信息）
@bp.route('/display', methods='GET')
def display():
    return jsonify({"msg": 1})


# 新建 传入 （账号 文件内容） 返回 （状态）
@bp.route('/create', methods='POST')
def create():
    username = request.json.get("username")
    content = request.json.get("content")

    db = get_db()
    user_id = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    db.execute('INSERT INTO document (author_id, folder_id, content) VALUES (?, ?, ?)',
               (user_id, 'default', content))
    db.commit()

    return jsonify({"msg": 1})


# 传入 （账号 文件id 文件内容） 返回 （状态）
@bp.route('/revise', methods='PUT')
def revise():
    return jsonify({"msg": 1})


# 文件夹详情页面 传入 （账号 文件夹id） 返回 （文件夹所有包含的笔记 以及 信息）
@bp.route('/unfold', methods='GET')
def unfold():
    username = request.args.get("username")
    folder_id = request.args.get("folder_id")

    db = get_db()
    user_id = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    docs = db.execute(
        'SELECT * FROM document WHERE author_id = ? and folder_id = ?', (user_id, folder_id)
    ).fetchall()
    '''
    ToDo: 返回文件夹所有包含的笔记以及信息
    '''

    return jsonify({"msg": 1})


# 文件详情页面chat 传入 （账号 问题内容） 返回 （问题对应答案）
@bp.route('/chat', methods='POST')
def chat():
    username = request.json.get("username")
    question = request.json.get("question")

    db = get_db()
    answer = db.execute(
        'SELECT answer FROM corpus WHERE qusetion = ?', (question,)
    ).fetchone()

    return jsonify({"answer": answer[0]})