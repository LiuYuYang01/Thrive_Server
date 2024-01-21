from datetime import datetime

from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class ArticleQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class ArticleBody(BaseModel):
    id: Optional[int]
    title: str = Field(default="大前端新趋势", description="文章标题")
    description: str = Field(default="文章摘要", description="文章摘要")
    content: str = Field(default="文章内容", description="文章内容")
    cover: str = Field(default="http://127.0.0.1:5000/1.jpg", description="文章封面")
    view: int = Field(default=10, description="文章浏览量")
    comment: int = Field(default=10, description="文章评论数量")
    cate: str = Field(default="大前端", description="文章分类")
    tag: str = Field(default="大前端,Python,java", description="文章标签")
    createtime: datetime = Field(default=datetime.now(), description="文章创建时间")


class ArticleBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
