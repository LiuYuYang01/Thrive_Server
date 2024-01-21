from datetime import datetime

from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class CommentQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class CommentBody(BaseModel):
    id: Optional[int]
    name: str = Field(default="神秘人", description="用户名称")
    avatar: str = Field(default="http://127.0.0.1:5000/1.jpg", description="用户头像")
    content: str = Field(default="评论内容", description="用户评论的内容")
    email: str = Field(default="3311118881@qq.com", description="用户邮箱")
    url: str = Field(default="http://127.0.0.1:5000", description="用户网站")
    aid: int = Field(default=1, description="该评论所属的文章ID")
    rid: int = Field(default=1, description="记录所有回复该评论的ID")
    audit: int = Field(default=1, description="该评论是否审核 审核成功：1 | 待审核：0")
    createtime: datetime = Field(default=datetime.now(), description="发布评论的时间")


class CommentBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
