from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class TagQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class TagBody(BaseModel):
    id: Optional[int]
    name: str = Field(default="大前端", description="标签名称")


class TagBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
