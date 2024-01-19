from flask import Blueprint, request

from src.model import db
from src.model.TagModel import TagModel
from src import siwa
from src.siwadoc.TagSiwa import TagQuery, TagBody, TagBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

tag = Blueprint("tag", __name__)


# 新增标签
@tag.route("/tag", methods=["POST"])
@siwa.doc(tags=["标签管理"], summary="新增标签", description="新增标签记得把id去掉，否则可能会导致重复id异常",
          body=TagBody)
def add():
    tag = request.json

    data = TagModel(**tag)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除标签
@tag.route("/tag/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["标签管理"], summary="删除标签", description="通过ID删除指定标签")
def drop(id):
    data = TagModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此标签")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除标签成功")


# 批量删除
@tag.route("/tag", methods=["DELETE"])
@siwa.doc(tags=["标签管理"], summary="批量删除标签", description="[1,2,3] 删除ID为1、2、3的数据", body=TagBodyId)
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = TagModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的标签")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除标签成功")


# 编辑标签
@tag.route("/tag", methods=["PATCH"])
@siwa.doc(tags=["标签管理"], summary="编辑标签", body=TagBody)
def edit():
    tag = request.json

    data = TagModel.query.filter_by(id=tag["id"]).update(tag)

    if not data:
        return Result(400, "编辑失败：没有此标签")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取标签详情
@tag.route("/tag/<int:id>")
@siwa.doc(tags=["标签管理"], summary="获取标签详情", resp=TagBody)
def get(id):
    data = TagModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此标签")

    return Result(200, "获取标签详情成功", data.to())


# 获取标签列表
@tag.route("/tag")
@siwa.doc(tags=["标签管理"], summary="获取标签列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=TagQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的标签在最前面排序
    paginate = TagModel.query.paginate(page=page, per_page=size, error_out=False)

    data = {
        "result": [k.to() for k in paginate],
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取标签列表成功", data)
