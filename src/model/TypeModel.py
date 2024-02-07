from src.model import db
from src.utils.model import BaseModel


class TypeModel(BaseModel):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # 类型名称
