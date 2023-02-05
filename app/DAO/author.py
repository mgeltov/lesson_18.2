# CRUD - create, read, update, delete
from app.DAO.model.author import Author


class AuthorDAO:
    def __int__(self, session):
        self.session = session

#   C - create
    def create(self, data):
        author = Author(**data)

        self.session.add(author)
        self.session.commit()

        return author

#   R - read
    def get_one(self, aid):
        return self.session.query(Author).get(aid)

    def get_all(self):
        return self.session.query(Author).all()

#   U - update
    def update(self, author):
        self.session.add(author)
        self.session.commit()

        return author

#   D - delete
    def delete(self, aid):
        author = self.get_one(aid)
        self.session.delete(author)
        self.session.commit()
