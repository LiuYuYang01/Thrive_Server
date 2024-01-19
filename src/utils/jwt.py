from flask import request
from src.utils.response import Result

from functools import wraps
import jwt

# from app.config import SecretKey
from src import app

# 从配置中加载秘钥
SecretKey = app.config["SECRET_KEY"]

# 定义装饰器函数，用于验证 token 的有效性
class ExpiredSignatureError:
    pass


def TokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # 从请求头或查询参数中获取 token
        if 'Authorization' in request.headers:
            parts = request.headers['Authorization'].split()
            if len(parts) == 2 and parts[0] == 'Bearer':
                token = parts[1]
        elif 'token' in request.args:
            token = request.args.get('token')

        # 如果找到 token，验证其有效性
        if token:
            try:
                payload = jwt.decode(token, SecretKey, algorithms=['HS256'])
                # 验证成功，可以继续处理请求
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return Result(401, "过期的Token")
            except jwt.InvalidTokenError:
                return Result(401, "无效的Token")

        # 没有找到 token
        return Result(401, "不存在的Token")

    return decorated
