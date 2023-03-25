"""
文件详情页面：查看（展示文件具体内容和summary）、修改、新建文件，, chat
Pending:
revise: display(),chat()

"""

from flask import (
    Blueprint, request, jsonify
)
from flask_cors import CORS
from flaskr.db import get_db
from flaskr.chatUtil import *

bp = Blueprint('document', __name__, url_prefix='/document')
cors = CORS(bp)


# 传入 （账号 文件id） 返回 （文件具体内容）
@bp.route('/display', methods=['GET', ])
def display():
    username = request.json.get("username")
    doc_id = request.json.get("file_id")

    db = get_db()
    doc = db.execute(
        'SELECT * FROM document WHERE id = ?', (doc_id,)
    ).fetchone()
    # list(doc) [id,author_id,folder_id,content,created]
    return jsonify({"docs": list(doc)})


# 新建 传入 （账号 文件内容） 返回 （状态）
@bp.route('/create', methods=['POST', ])
def create():
    username = request.json.get("username")
    content = request.json.get("content")
    foldername = 'default'

    db = get_db()
    user = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    folder = db.execute(
        'SELECT * FROM folder WHERE author_id = ? and foldername = ?', (user['id'], foldername)
    ).fetchone()
    db.execute('INSERT INTO document (author_id, folder_id, content) VALUES (?, ?, ?)',
               (user['id'], folder['id'], content))
    db.commit()

    return jsonify({"msg": 1})


# 传入 （账号 文件id 文件内容） 返回 （状态）
@bp.route('/revise', methods=['PUT', ])
def revise():
    username = request.json.get("username")
    doc_id = request.json.get("file_id")
    content = request.json.get("content")

    db = get_db()
    db.execute('UPDATE document set content = ? where id = ?', (content, doc_id))
    db.commit()

    return jsonify({"msg": 1})


# 文件夹详情页面 传入 （账号 文件夹id） 返回 （文件夹所有包含的笔记 以及 信息）
@bp.route('/unfold', methods=['GET', ])
def unfold():
    username = request.args.get("username")
    folder_id = request.args.get("folder_id")

    db = get_db()
    user = db.execute(
        'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone()
    doc = db.execute(
        'SELECT * FROM document WHERE author_id = ? and folder_id = ?', (user['id'], folder_id)
    ).fetchall()

    # docs [[id,author_id,folder_id,content,created],[],...]
    docs = [list(item) for item in doc]

    return jsonify({"docs": docs})


# 文件详情页面chat 传入 （账号, 问题内容） 返回 （问题对应答案）
@bp.route('/chat', methods=['GET', 'POST'])
def chat():
    username = request.json.get("username")
    question = request.json.get("question")
    # doc_id = request.json.get("doc_id")

    db = get_db()
    document = db.execute(
        'SELECT * FROM document WHERE id = ?', (1,)
    ).fetchall()

    prompt = "According to the passage below, answer my question: " + question + ", the passage is here: " + \
             document['content']
    answer = chatUtil(prompt)
    return jsonify({"answer": answer})
