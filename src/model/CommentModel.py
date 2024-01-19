from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class CommentModel(BaseModel):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # 用户名称
    avatar = db.Column(db.String(255), nullable=False)  # 用户头像
    content = db.Column(db.String(500), nullable=False)  # 评论内容
    email = db.Column(db.String(100), nullable=False)  # 邮箱
    url = db.Column(db.String(500), nullable=False)  # 地址
    aid = db.Column(db.Integer, nullable=False)  # 该评论所在的文章id
    rid = db.Column(db.Integer, nullable=False)  # 所有回复这条评论的id
    audit = db.Column(db.Integer, nullable=False)  # 评论是否审核成功
    crearetime = db.Column("creare_time", db.DateTime, default=datetime.utcnow)  # 创建时间
