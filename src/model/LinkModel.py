from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class LinkModel(BaseModel):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))  # 标题
    description = db.Column(db.String(255))  # 描述
    email = db.Column(db.String(100))  # 邮箱
    image = db.Column(db.String(255))  # 图片
    url = db.Column(db.String(500))  # 跳转地址
    type = db.Column(db.String(100))  # 跳转地址
    createtime = db.Column("create_time", db.DateTime, default=datetime.utcnow)  # 创建时间
