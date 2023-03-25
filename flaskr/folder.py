"""
文件夹：查看文件夹
Pending: 无
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('folder', __name__, url_prefix='/folder')
cors = CORS(bp)


# 传入（账号 current page 页码 每一页文件夹数） 返回 （账号所拥有的文件夹）
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
    folder = db.execute(
        'SELECT * FROM folder WHERE author_id = ? limit ? offset ? ', (str(user['id']),int(number),\
                                                                             (int(offset)-1)*int(number) )
    ).fetchmany()

    # folders [[id,author_id,foldername,created],[],...]
    folders = [list(item) for item in folder]

    return jsonify({"folder": folders, 'msg':1})
