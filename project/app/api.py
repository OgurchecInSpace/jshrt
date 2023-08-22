from flask import Flask, request

from app.models import UrlData
from app import db, get_url, Config

api = Flask(__name__)
api.config.from_object(Config)
db.init_app(api)


@api.route('/', methods=['GET', 'POST'])
def get_short_url():
    url = request.args.get('url')
    if url is None:
        return 'nothing here'
    # Проверяем на наличие протокола соединения в URL
    # (чтобы впоследствии перенаправление шло на внешний сайт)
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    # И если короткого URL для ссылки ещё нет, то генерируем и заносим в базу данных
    if UrlData.query.filter_by(url=url).first() is None:
        short_url = get_url()
        new_url = UrlData(url=url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()
    # Если есть, то просто берём его
    else:
        short_url = UrlData.query.filter_by(url=url).first().short_url
    return short_url


@api.errorhandler(404)
def not_found_error(error):
    return '404'
