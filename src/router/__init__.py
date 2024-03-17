from src.utils.response import Result

from .ProjectRouter import project
from .UserRouter import user
from .ArticleRouter import article
from .TagRouter import tag
from .SwiperRouter import swiper
from .LinkRouter import link
from .CommentRouter import comment
from .CateRouter import cate
from .ResRouter import res
from .LinkTypeRouter import link_type
from .ChatRouter import chat

from src import app

from flask_cors import CORS

# 注册CORS, "/*" 允许访问所有api
CORS(app, resources=r'/*')

urlPrefix = app.config["URL_PREFIX"]

app.register_blueprint(project, url_prefix=urlPrefix)
app.register_blueprint(user, url_prefix=urlPrefix)
app.register_blueprint(res, url_prefix=urlPrefix)
app.register_blueprint(cate, url_prefix=urlPrefix)
app.register_blueprint(article, url_prefix=urlPrefix)
app.register_blueprint(comment, url_prefix=urlPrefix)
app.register_blueprint(link, url_prefix=urlPrefix)
app.register_blueprint(swiper, url_prefix=urlPrefix)
app.register_blueprint(tag, url_prefix=urlPrefix)
app.register_blueprint(link_type, url_prefix=urlPrefix)
app.register_blueprint(chat, url_prefix=urlPrefix)


# 捕获全局HTTP请求异常
@app.errorhandler(Exception)
def GlobalError(e):
    # 获取异常类型
    print(f"程序异常：{e}")

    if str(e).find("MySQLdb.IntegrityError") != -1: return Result(500, f"数据库异常：可能是数据重复")

    # 返回适当的错误响应
    return Result(500, f"程序异常：{e}")
