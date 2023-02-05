from flask import request
from flask_restx import Resource, Namespace
from app.DAO.model.author import AuthorSchema
from app.container import author_service

authors_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

@authors_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        author_service.create(req_json)
        return "", 201


@authors_ns.route('/<int:aid>')
class AuthorView(Resource):
    def get(self, aid):
        try:
            author = author_service.get_one(aid)
            return author_schema.dump(author), 200
        except Exception as e:
            return str(e), 404

    def put(self, aid):
        req_json = request.json

        req_json['id'] = aid
        author_service.update(req_json)

        return "", 204


    def patch(self, aid):
        req_json = request.json

        req_json['id'] = aid
        author_service.part_update(req_json)

        return "", 204


    def delete(self, aid):
        author_service.delete(aid)

        return "", 204
