from flask_sqlalchemy import SQLAlchemy

from src.config.env import switch

db = None


# 创建SQLAlchemy实例
def CreateSQLAlchemy(app, type):
    global db

    # 选择开发 / 线上环境
    env = switch[type]

    # 将配置信息加载到 Flask 应用程序中
    app.config.from_object(env)

    # 保存起来，方便其他地方使用
    db = SQLAlchemy(app)

    return db
