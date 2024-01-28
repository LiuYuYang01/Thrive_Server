from pydantic import BaseModel, Field
from typing import Optional, Any


class ResBody(BaseModel):
    file: Any = Field(description="请上传文件")
    target: Optional[str] = Field(default="default", description="指定文件上传的目录")


class FileBody(BaseModel):
    files: list = Field(default=["/image/2024/1/111.jpg", "/image/2024/1/222.jpg"], description="指定需要删除的文件路径")
