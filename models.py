from dbase import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)  # будем хранить хэш пароля

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.username)

    @staticmethod
    def add(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(80), unique=False, nullable=True)  # пусть текст можно будет оставить пустым
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user_id - вторичный ключ, который связывает 2 таблицы
    # Пользователь пишет Новость(их может быть несколько), Новость принадлежит Пользователю, свзяь Один-Ко-Многим
    user = db.relationship('User', backref=db.backref('books_list', lazy=True))
    # ссылка на модель (класс) выше
    # для User возвращает список его новостей по .user_books

    def __repr__(self):
        return '<Books {} {} {}>'.format(self.id, self.title, self.user_id)

    @staticmethod
    def add(title, content, user):
        books = Books(title=title, content=content, user=user)
        db.session.add(books)
        db.session.commit()
        return books

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id
        }

