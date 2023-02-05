from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from app.database import db


class Author(db.Model):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birth_year = Column(Integer)


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    birth_year = fields.Int()