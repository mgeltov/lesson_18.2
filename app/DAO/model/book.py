from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from app.database import db


class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    year = Column(Integer)

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    year = fields.Int()
