from app.DAO.author import AuthorDAO


class AuthorService:
    def __init__(self, dao: AuthorDAO):
        self.dao = dao

    def create(self, data):
        return self.dao.create(data)

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def update(self, data):

        aid = data.get('id')
        author = self.get_one(aid)

        author.name = data.get("name")
        author.birth_year = data.get("birth_year")

        self.dao.update(author)

    def part_update(self, data):
        aid = data.get('id')
        author = self.get_one(aid)

        if 'name' in data:
            author.name = data.get("name")
        if 'birth_year' in data:
            author.birth_year = data.get("birth_year")

        self.dao.update(author)

    def delete(self, aid):
        return self.dao.delete(aid)
