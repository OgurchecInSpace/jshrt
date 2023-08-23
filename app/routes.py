from app import app, db, get_url, Config
from flask import render_template, flash, redirect, url_for, request, abort, Request

from app.models import UrlData


# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    # Если получен запрос от браузера
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if data is not None:
            url = data['url']
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
    return render_template('index.html')


# Страницы коротких ссылок, которые сразу перенаправляют на изначальные сайты
@app.route('/<short_url>')
def request_short_url(short_url):
    # Получаем элемент с переданным коротким URL
    item = UrlData.query.filter_by(short_url=f'{Config.ADDRESS}/{short_url}').first()
    # Если существует такой элемент, то просто перенаправляем браузер по его настоящему URL
    if item is not None:
        return redirect(item.url)
    # Иначе возвращаем ошибку, сообщающую, что к данному короткому URL не привязан никакой настоящий URL
    else:
        return abort(404)


@app.route('/api')
def api():
    url = request.args.get('url')
    if url is None:
        return render_template('api.html', address=Config.ADDRESS)
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


