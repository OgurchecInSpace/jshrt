from app import app, db, clear_db
from app.models import UrlData, Slices
from config import Config
from app.api import api
from threading import Thread


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'UrlData': UrlData, 'Slices': Slices, 'clear_db': clear_db}


if __name__ == "__main__":
    from waitress import serve

    print(Config.HOST)
    # radmin ip 26.160.84.169
    # Запуск отдельного потока с API
    Thread(target=lambda: serve(api, host=Config.HOST, port=Config.API_PORT)).start()
    # Основной поток именно сайта
    serve(app, host=Config.HOST, port=Config.PORT)
