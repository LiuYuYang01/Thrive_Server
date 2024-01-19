from datetime import datetime, date
from decimal import Decimal

from sqlalchemy.orm import class_mapper

from src.model import db


def format_data(data):
    # 格式化数据,处理json无法序列化的数据
    if isinstance(data, datetime):
        return data.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(data, date):
        return data.strftime("%Y-%m-%d")
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data


class BaseModel(db.Model):
    # 生成抽象模型，不会创建模型对应的表,减少重复代码
    __abstract__ = True

    def to(self):
        return {p.key: format_data(getattr(self, p.key)) for p in class_mapper(self.__class__).iterate_properties}
