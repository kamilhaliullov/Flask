"""
Точка входа

Здесь инициализируются все настройки, подключения к БД, приложение flask и маршрутизатор (router)

После инициализации запускается вебсервер
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controller import init_route
from dbase import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_route(app, db)

app.run(port=8080, host='127.0.0.1')
