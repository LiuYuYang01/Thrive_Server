from src.config import BaseConfig


# 开发环境
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liuyuyang@127.0.0.1:3306/ThriveX'


# 生产环境
class ProduceConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liuyuyang@127.0.0.1:3306/ThriveX'


# 选择环境
switch = {
    "dev": DevelopConfig,
    "pro": ProduceConfig
}
