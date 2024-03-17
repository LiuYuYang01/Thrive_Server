from src.model import db
from src.utils.model import BaseModel


class ChatModel(BaseModel):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer)  # 房间号
    data = db.Column(db.JSON)  # 聊天内容
