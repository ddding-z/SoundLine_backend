"""
文件详情页面：查看、修改、新建文件； chat
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('document', __name__, url_prefix='/document')
cors = CORS(bp)


# 传入 （账号 文件id） 返回 （文件具体内容和信息）
@bp.route('/display', methods=('GET', 'POST'))
def display():
    return jsonify({"msg": 1})


# 新建 传入 （账号 文件内容） 返回 （状态）
@bp.route('/display', methods=('GET', 'POST'))
def create():
    return jsonify({"msg": 1})


# 文件夹详情页面 传入 （账号 文件夹id） 返回 （文件夹所有包含的笔记 以及 信息）
@bp.route('/unfold', methods=('GET', 'POST'))
def unfold():
    return jsonify({"msg": 1})


# 文件详情页面chat 传入 （账号 问题内容） 返回 （问题对应答案）
@bp.route('/chat', methods=('GET', 'POST'))
def chat():
    return jsonify({"msg": 1})



