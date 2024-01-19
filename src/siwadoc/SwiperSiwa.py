from datetime import datetime

from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class SwiperQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class SwiperBody(BaseModel):
    id: Optional[int]
    title: str = Field(default="大前端新趋势", description="轮播图标题")
    description: str = Field(default="轮播图摘要", description="轮播图摘要")
    image: str = Field(default="http://127.0.0.1:5000/1.jpg", description="轮播图")
    url: str = Field(default="http://127.0.0.1:5000", description="轮播图跳转地址")
    crearetime: datetime = Field(default=datetime.now(), description="轮播图创建时间")


class SwiperBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
