from datetime import datetime

from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional


class UserQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class LoginBody(BaseModel):
    username: str = Field(default="liuyuyang", description="用户名")
    password: str = Field(default="123123", description="密码")


class UserBody(BaseModel):
    id: Optional[int]
    username: str = Field(default="liuyuyang", description="用户名")
    password: str = Field(default="123123", description="密码")
    name: str = Field(default="YuYang", description="用户名称")
    email: str = Field(default="3311118881@qq.com", description="用户邮箱")
    avatar: str = Field(default="https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640", description="用户头像")
    info: str = Field(default="再渺小的星光，也有属于他的光芒!", description="用户介绍")
    role: str = Field(default="admin", description="用户组")
    createtime: datetime = Field(default=datetime.now(), description="用户加入时间")


class UserBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
