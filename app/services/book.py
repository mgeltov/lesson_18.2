from app.DAO.book import BookDAO


class BookService:
    def __init__(self, dao: BookDAO):
        self.dao = dao

    def create(self, data):
        return self.dao.create(data)

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def update(self, data):

        bid = data.get('id')
        book = self.get_one(bid)

        book.name = data.get("name")
        book.year = data.get("year")

        self.dao.update(book)

    def part_update(self, data):
        aid = data.get('id')
        book = self.get_one(aid)

        if 'name' in data:
            book.name = data.get("name")
        if 'year' in data:
            book.birth_year = data.get("year")

        self.dao.update(book)

    def delete(self, bid):
        return self.dao.delete(bid)
