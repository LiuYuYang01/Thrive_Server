from pydantic import BaseModel, Field
from typing import Optional, Any


class ResBody(BaseModel):
    file: Any = Field(description="请上传文件")
    target: Optional[str] = Field(default="default", description="指定文件上传的目录")

class PathBody(BaseModel):
    path: str = Field(default="/image/2024/1/123.jpg", description="指定需要删除的文件路径")
