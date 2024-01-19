from flask import Flask
from flask_siwadoc import SiwaDoc

app = Flask(__name__, static_url_path="/")
siwa = SiwaDoc(app, title="Flask Siwadoc", description="一个自动生成openapi文档的库", version="2.0")


def CreateApp(env):
    from src.model import CreateSQLAlchemy
    db = CreateSQLAlchemy(app, env)

    # 在应用上下文中运行应用
    with app.app_context():
        # 删除所有继承自db.Model的表
        # db.drop_all()
        # 创建所有继承自db.Model的表
        db.create_all()

    # 配置网站资源存放位置
    app.static_folder = app.config["UPLOAD_PATH"][1:]

    # 加载路由
    from src import router

    return app
