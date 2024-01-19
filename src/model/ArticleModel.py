from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class ArticleModel(BaseModel):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))  # 文章标题
    description = db.Column(db.String(200))  # 文章摘要
    content = db.Column(db.Text)  # 文章内容
    cover = db.Column(db.String(300))  # 文章封面
    view = db.Column(db.Integer, default=0)  # 文章浏览量
    comment = db.Column(db.Integer, default=0)  # 评论数量
    cate = db.Column(db.String(255))  # 文章分类
    tag = db.Column(db.String(100))  # 文章标签
    crearetime = db.Column("creare_time", db.DateTime, default=datetime.utcnow)  # 创建时间
