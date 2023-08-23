from app import app, db, clear_db
from app.models import UrlData, Slices
from config import Config


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'UrlData': UrlData, 'Slices': Slices, 'clear_db': clear_db}


if __name__ == "__main__":
    from waitress import serve

    print(Config.HOST)
    serve(app, host=Config.HOST, port=Config.PORT)
