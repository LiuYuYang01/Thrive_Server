from pydantic import BaseModel, Field


class ProjectBody(BaseModel):
    title: str = Field(default="Thrive", description="网站标题")
    subhead: str = Field(default="花有重开日, 人无再少年", description="网站副标题")
    logo: str = Field(default="https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640", description="网站LOGO")
    description: str = Field(default="记录前端、Python、Java点点滴滴", description="网站描述")
    keyword: str = Field(default="Thrive,前端,Python,Java", description="网站SEO关键词")
