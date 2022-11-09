from app.errors import bp
from flask import render_template


@bp.app_errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html'), 400


@bp.app_errorhandler(403)
def bad_request(error):
    return render_template('errors/403.html'), 403


@bp.app_errorhandler(404)
def bad_request(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(405)
def bad_request(error):
    return render_template('errors/405.html'), 405

    @bp.app_errorhandler(500)
    def internal_error(error):
        # db.session.rollback()
        return render_template('errors/500.html'), 500
