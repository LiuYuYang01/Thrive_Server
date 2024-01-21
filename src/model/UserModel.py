from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class UserModel(BaseModel):
    # 创建用户表
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100))
    avatar = db.Column(db.String(255))
    info = db.Column(db.String(255))
    role = db.Column(db.String(50), default="user")
    createtime = db.Column("create_time", db.DateTime, default=datetime.utcnow)  # 创建时间