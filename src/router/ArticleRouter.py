from flask import Blueprint, request
from sqlalchemy import text

from src.model import db
from src.model.ArticleModel import ArticleModel
from src.model.CateModel import CateModel
from src import siwa
from src.siwadoc.ArticleSiwa import ArticleQuery, ArticleBody, ArticleBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

article = Blueprint("article", __name__)


# 新增文章
@article.route("/article", methods=["POST"])
@siwa.doc(tags=["文章管理"], summary="新增文章", description="新增文章记得把id去掉，否则可能会导致重复id异常",
          body=ArticleBody)
@TokenRequired
def add():
    article = request.json

    # 将分类数组转换为字符串
    article["cids"] = ",".join([str(k) for k in article["cids"]])

    data = ArticleModel(**article)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除文章
@article.route("/article/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["文章管理"], summary="删除文章", description="通过ID删除指定文章")
@TokenRequired
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
@TokenRequired
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
@TokenRequired
def edit():
    article = request.json

    # 将分类数组转换为字符串
    article["cids"] = ",".join([str(k) for k in article["cids"]])

    data = ArticleModel.query.filter_by(id=article["id"])

    if not data:
        return Result(400, "编辑失败：没有此文章")

    data.update({
        "cids": article["cids"],
        "comment": article["comment"],
        "content": article["content"],
        "cover": article["cover"],
        "description": article["description"],
        "tag": article["tag"],
        "title": article["title"],
        "view": article["view"]
    })

    db.session.commit()

    return Result(200, "编辑成功")


# 获取文章详情
@article.route("/article/<int:id>")
@siwa.doc(tags=["文章管理"], summary="获取文章详情", resp=ArticleBody)
def get(id):
    data = ArticleModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此文章")

    article = data.to()
    article["cate"] = []
    # 将cid字符串转换为列表，并将字符串列表转换为数值列表
    article["cids"] = [int(k) for k in article["cids"].split(",")]

    # 循环每一项的分类id，找出文章所对应的那一个
    for id in article["cids"]:
        cate = CateModel.query.filter_by(id=id).first().to()
        article["cate"].append(cate)

    return Result(200, "获取文章详情成功", article)


# 获取文章列表
@article.route("/article")
@siwa.doc(tags=["文章管理"], summary="获取文章列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=ArticleQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的文章在最前面排序
    paginate = ArticleModel.query.order_by(ArticleModel.createtime.desc()).paginate(page=page, per_page=size,
                                                                                    error_out=False)

    result = []

    # 关联分类表
    for article in paginate:
        article = article.to()

        article["cate"] = []
        # 将cid字符串转换为列表，并将字符串列表转换为数值列表
        article["cids"] = [int(k) for k in article["cids"].split(",")]

        # 循环每一项的分类id，找出文章所对应的那一个
        for id in article["cids"]:
            cate = CateModel.query.filter_by(id=id).first().to()
            article["cate"].append(cate)

        result.append(article)

    data = {
        "result": result,
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取文章列表成功", data)


# 获取指定分类中的所有文章
@article.route("/article/<mark>")
@siwa.doc(tags=["文章管理"], summary="获取指定分类中的所有文章", description="根据分类的标识查询",
          query=ArticleQuery)
def articleCate(mark):
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 自定义sql查询
    sql_query = text(
        "select a.* from article a, cate c where find_in_set(c.id,a.cids) and c.mark = :mark limit :size offset :offset")
    sql_result = db.session.execute(sql_query, {'mark': mark, 'size': size, 'offset': (page - 1) * size})

    result = []
    for row in sql_result:
        cate = []

        # 循环每一项的分类id，找出文章所对应的那一个
        for id in [int(k) for k in row.cids.split(",")]:
            cate.append(CateModel.query.filter_by(id=id).first().to())

        result.append({"id": row.id, "title": row.title, "description": row.description, "content": row.content,
                       "cover": row.cover,
                       "view": row.view, "comment": row.comment, "cids": row.cids, "cate": cate, "tag": row.tag,
                       "createTime": row.create_time})

    data = {
        "result": result,
        "page": page,
        "size": size,
        "pages": 0,
        "total": len(result),
        "prev": False,
        "next": False
    }

    return Result(200, "获取文章列表成功", data)
