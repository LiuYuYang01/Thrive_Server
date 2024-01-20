from src.model import db
from src.utils.model import BaseModel


class CateModel(BaseModel):
    __tablename__ = 'cate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    icon = db.Column(db.String(10))
    url = db.Column(db.String(255))
    mark = db.Column(db.String(30), unique=True)
    level = db.Column(db.Integer, default=0)
