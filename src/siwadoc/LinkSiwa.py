from datetime import datetime

from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class LinkQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class LinkBody(BaseModel):
    id: Optional[int]
    title: str = Field(default="YuYang", description="网站标题")
    description: str = Field(default="逐渐强大的全栈开发工程师", description="网站介绍")
    email: str = Field(default="3311118881@qq.com", description="网站邮箱")
    image: str = Field(default="http://127.0.0.1:5000/1.jpg", description="网站图标")
    url: str = Field(default="http://127.0.0.1:5000", description="网站跳转地址")
    type: str = Field(default="生活类", description="网站类型")
    crearetime: datetime = Field(default=datetime.now(), description="网站加入时间")


class LinkBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
