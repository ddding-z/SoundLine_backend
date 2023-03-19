"""
Auth：登录、注册
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS, cross_origin
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
cors = CORS(bp)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        db = get_db()

        if not username:
            return jsonify({"msg": 0})
        elif not password:
            return jsonify({"msg": 0})
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            return jsonify({"msg": 0})

        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()
        return jsonify({"msg": 1})


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            return jsonify({"msg": 0})
        elif not check_password_hash(user['password'], password):
            return jsonify({"msg": 0})

        session.clear()
        session['user_id'] = user['id']
        return jsonify({"msg": 1, "username": username})


