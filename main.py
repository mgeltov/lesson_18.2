from flask import Flask
from flask_restx import Api

from app.DAO.model.author import Author
from app.DAO.model.book import Book
from app.config import Config
from app.database import db
from app.views.authors import authors_ns
from app.views.books import books_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(books_ns) # books
    api.add_namespace(authors_ns) # authors

def load_data():
    b1 = Book(id=1, name='War and Peace', year=1869)
    b2 = Book(id=2, name='Gambler', year=1866)

    a1 = Author(id=1, name='Leo Tolstoy', birth_year=1828)
    a2 = Author(id=2, name='Fedor Dostoevskiy', birth_year=1821)

    db.drop_all()
    db.create_all()

    with db.session.begin():
        db.session.add_all([b1, b2])
        db.session.add_all([a1, a2])
        db.session.commit()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()
