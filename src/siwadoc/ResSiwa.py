from pydantic import BaseModel, Field
from typing import Optional, Any


class ResBody(BaseModel):
    file: Any = Field(description="请上传文件")
    tagger: Optional[str] = Field(default="image", description="指定文件上传的目录")
