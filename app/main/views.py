from app.main import bp


@bp.route('/')
def test():
    return "Hello World"
