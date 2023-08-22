import os
import socket

basedir = os.path.abspath(os.path.dirname(__file__))


# Все данные, используемые для конфигурации приложения
# (их можно менять (но некоторые не желательно (я сам не знаю, какие нельзя (помогите))))
class Config:
    # print(socket.gethostbyname_ex(socket.gethostname()))
    HOST = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
    PORT = 8080
    ADDRESS = f'{HOST}:{PORT}'  # Возможно, это будет заменено настоящим доменом когда-нибудь
    API_PORT = 9090
    API_ADDRESS = f'{HOST}:{API_PORT}'  # И это тоже
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

