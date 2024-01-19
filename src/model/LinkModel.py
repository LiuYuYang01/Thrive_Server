from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class LinkModel(BaseModel):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # 标题
    description = db.Column(db.String(255), nullable=False)  # 描述
    email = db.Column(db.String(100), nullable=False)  # 邮箱
    image = db.Column(db.String(255), nullable=False)  # 图片
    url = db.Column(db.String(500), nullable=False)  # 跳转地址
    type = db.Column(db.String(100), nullable=False)  # 跳转地址
    crearetime = db.Column("creare_time", db.DateTime, default=datetime.utcnow)  # 创建时间
