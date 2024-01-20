from flask import Blueprint, request

from src.model import db
from src.model.ArticleModel import ArticleModel
from src import siwa
from src.siwadoc.ArticleSiwa import ArticleQuery, ArticleBody, ArticleBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

article = Blueprint("article", __name__)


# 新增文章
@article.route("/article", methods=["POST"])
@siwa.doc(tags=["文章管理"], summary="新增文章", description="新增文章记得把id去掉，否则可能会导致重复id异常",
          body=ArticleBody)
def add():
    article = request.json

    data = ArticleModel(**article)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除文章
@article.route("/article/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["文章管理"], summary="删除文章", description="通过ID删除指定文章")
def drop(id):
    data = ArticleModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此文章")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除文章成功")


# 批量删除
@article.route("/article", methods=["DELETE"])
@siwa.doc(tags=["文章管理"], summary="批量删除文章", description="[1,2,3] 删除ID为1、2、3的数据", body=ArticleBodyId)
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = ArticleModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的文章")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除文章成功")


# 编辑文章
@article.route("/article", methods=["PATCH"])
@siwa.doc(tags=["文章管理"], summary="编辑文章", body=ArticleBody)
def edit():
    article = request.json

    data = ArticleModel.query.filter_by(id=article["id"]).update(article)

    if not data:
        return Result(400, "编辑失败：没有此文章")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取文章详情
@article.route("/article/<int:id>")
@siwa.doc(tags=["文章管理"], summary="获取文章详情", resp=ArticleBody)
def get(id):
    data = ArticleModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此文章")

    return Result(200, "获取文章详情成功", data.to())


# 获取文章列表
@article.route("/article")
@siwa.doc(tags=["文章管理"], summary="获取文章列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=ArticleQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的文章在最前面排序
    paginate = ArticleModel.query.order_by(ArticleModel.crearetime.desc()).paginate(page=page, per_page=size, error_out=False)

    data = {
        "result": [k.to() for k in paginate],
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取文章列表成功", data)
