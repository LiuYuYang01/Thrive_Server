from flask import Blueprint, request

from src.model import db
from src.model.LinkModel import LinkModel
from src import siwa
from src.model.TypeModel import TypeModel
from src.siwadoc.LinkSiwa import LinkQuery, LinkBody, LinkBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

link = Blueprint("link", __name__)


# 新增网站
@link.route("/link", methods=["POST"])
@siwa.doc(tags=["网站管理"], summary="新增网站", description="新增网站记得把id去掉，否则可能会导致重复id异常",
          body=LinkBody)
@TokenRequired
def add():
    link = request.json

    data = LinkModel(**link)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除网站
@link.route("/link/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["网站管理"], summary="删除网站", description="通过ID删除指定网站")
@TokenRequired
def drop(id):
    data = LinkModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此网站")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除网站成功")


# 批量删除
@link.route("/link", methods=["DELETE"])
@siwa.doc(tags=["网站管理"], summary="批量删除网站", description="[1,2,3] 删除ID为1、2、3的数据", body=LinkBodyId)
@TokenRequired
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = LinkModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的网站")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除网站成功")


# 编辑网站
@link.route("/link", methods=["PATCH"])
@siwa.doc(tags=["网站管理"], summary="编辑网站", body=LinkBody)
@TokenRequired
def edit():
    link = request.json

    data = LinkModel.query.filter_by(id=link["id"]).update(link)

    if not data:
        return Result(400, "编辑失败：没有此网站")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取网站详情
@link.route("/link/<int:id>")
@siwa.doc(tags=["网站管理"], summary="获取网站详情", resp=LinkBody)
def get(id):
    data = LinkModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此网站")

    data = data.to()
    data["type"] = TypeModel.query.filter_by(id=data["type"]).first().to()["name"]

    return Result(200, "获取网站详情成功", data)


# 获取网站列表
@link.route("/link")
@siwa.doc(tags=["网站管理"], summary="获取网站列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=LinkQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的网站在最前面排序
    paginate = LinkModel.query.order_by(LinkModel.createtime.desc()).paginate(page=page, per_page=size, error_out=False)

    result = [k.to() for k in paginate]

    for k in result:
        k["type"] = TypeModel.query.filter_by(id=k["type"]).first().to()["name"]

    data = {
        "result": result,
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取网站列表成功", data)
