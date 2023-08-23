from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Все основные штуки для работы приложения
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Slices, UrlData  # Модели стоят позже db и прочего чтобы не было цикличного импорта


# Генерация короткого URL.
# Принцип работы:
# Имеется строка с символами, из которых генерируется короткий URL. Так как генератор нельзя сериализовать, то создаём
# индексы, которые указывают на буквы, из которых был собрал последний короткий URL. Изначально все индексы равны 0.
def _generate_urls():
    url_slices = Slices.query.first()  # Получаем срезы
    if not url_slices:
        url_slices = Slices(s1=0, s2=0, s3=0, s4=0, s5=0, s6=0)
        db.session.add(url_slices)
        db.session.commit()

    parts = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    list_slices = [getattr(Slices.query.first(), f's{n}') for n in range(1, 7)]
    while True:
        list_slices[-1] += 1

        # Блок с проверкой на то, что какое-либо из значений не вышло за пределы
        for index, s in enumerate(list_slices[1:], start=1):
            if s >= len(parts):
                list_slices[index] = 0
                list_slices[index - 1] += 1
        s1, s2, s3, s4, s5, s6 = list_slices

        # Собственно, сгенерированный URL
        short_url = f'{Config.ADDRESS}/{parts[s1] + parts[s2] + parts[s3] + parts[s4] + parts[s5] + parts[s6]}'

        # Замена полей sN у объекта url_slices на аналогичные, но прошедшие обработку
        url_slices = Slices.query.first()
        url_slices.s1 = s1
        url_slices.s2 = s2
        url_slices.s3 = s3
        url_slices.s4 = s4
        url_slices.s5 = s5
        url_slices.s6 = s6
        db.session.commit()

        yield short_url


urls = _generate_urls()


# Получение нового короткого URL
def get_url():
    new_url = next(urls)  # Получение нового URL
    return new_url


def clear_db():
    # Пробуем почистить таблицу с URL
    try:
        for data in UrlData.query.all():
            db.session.delete(data)
    except Exception as error:
        print(error)

    # Также пробуем почистить таблицу со срезами
    try:
        data = Slices.query.first()
        db.session.delete(data)
    except Exception as error:
        print(error)
    db.session.commit()


from app import routes, models, errors
