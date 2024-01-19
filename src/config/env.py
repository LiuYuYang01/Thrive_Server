from src.config import BaseConfig


# 开发环境
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123123@127.0.0.1:3306/student_py'


# 生产环境
class ProduceConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123123@127.0.0.1:3306/student'


# 选择环境
switch = {
    "dev": DevelopConfig,
    "pro": ProduceConfig
}
