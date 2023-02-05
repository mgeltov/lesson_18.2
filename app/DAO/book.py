#CRUD - create, read, update, delete
from app.DAO.model.book import Book


class BookDAO:
    def __int__(self, session):
        self.session = session


    #C - create
    def create(self, data):
        book = Book(**data)

        self.session.add(book)
        self.session.commit()

        return book


    # R - read
    def get_one(self, bid):
        return self.session.query(Book).get(bid)

    def get_all(self):
        return self.session.query(Book).all()


    #U - update
    def update(self, data):
        bid = data.get('id')
        book = self.get_one(bid)

        book.name = data.get("name")
        book.year = data.get("year")

        self.session.add(book)
        self.session.commit()

        return book


    def part_update(self, data):
        bid = data.get('id')
        book = self.get_one(bid)

        if 'name' in data:
            book.name = data.get("name")
        if 'year' in data:
            book.birth_year = data.get("year")

        self.session.add(book)
        self.session.commit()

        return book

    #D - delete
    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()