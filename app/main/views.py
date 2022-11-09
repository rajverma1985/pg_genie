from flask import abort

from app.main import bp


@bp.route('/')
def test():
    return "Hello World"


@bp.route('/admin')
def admin():
    abort(404)
