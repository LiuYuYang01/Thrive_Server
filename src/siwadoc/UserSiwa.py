from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class UserQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class UserBody(BaseModel):
    uid: Optional[int]
    username: str = Field(default="jack", description="用户名")
    password: str = Field(default="1234", description="密码")
    gender: bool = Field(default=True, description="性别")
    image: str = Field(default="https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640", description="头像")


class UserBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
