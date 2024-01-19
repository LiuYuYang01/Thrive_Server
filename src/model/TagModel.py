from src.model import db
from src.utils.model import BaseModel


class TagModel(BaseModel):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # 名称
