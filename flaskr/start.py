"""
Start：新建笔记、上传音频、查看用户笔记、文件夹
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('start', __name__, url_prefix='/start')
cors = CORS(bp)


# 新建笔记
@bp.route('/create', methods=('GET', 'POST'))
def create():
    return jsonify({"msg": 1})


# 上传音频并新建笔记
@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    return jsonify({"msg": 1})


# 笔记
@bp.route('/display', methods=('GET', 'POST'))
def display():
    return jsonify({"msg": 1})


# 文件夹
@bp.route('/directory', methods=('GET', 'POST'))
def directory():
    return jsonify({"msg": 1})
