from flask import Blueprint, request

from src.model import db
from src.model.TypeModel import TypeModel
from src.utils.jwt import TokenRequired
from src.utils.response import Result

link_type = Blueprint("link_type", __name__)


# 新增网站类型
@link_type.route("/link_type", methods=["POST"])
@TokenRequired
def add():
    link_type = request.json

    data = TypeModel(**link_type)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除网站类型
@link_type.route("/link_type/<int:id>", methods=["DELETE"])
@TokenRequired
def drop(id):
    data = TypeModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此网站类型")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除网站类型成功")


# 批量删除
@link_type.route("/link_type", methods=["DELETE"])
@TokenRequired
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = TypeModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的网站类型")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除网站类型成功")


# 编辑网站类型
@link_type.route("/link_type", methods=["PATCH"])
@TokenRequired
def edit():
    link_type = request.json

    data = TypeModel.query.filter_by(id=link_type["id"]).update(link_type)

    if not data:
        return Result(400, "编辑失败：没有此网站类型")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取网站类型详情
@link_type.route("/link_type/<int:id>")
def get(id):
    data = TypeModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此网站类型")

    data = data.to()
    data["link_type"] = TypeModel.query.filter_by(id=data["link_type"]).first().to()["name"]

    return Result(200, "获取网站类型详情成功", data)


# 获取网站类型列表
@link_type.route("/link_type")
def list():
    data = TypeModel.query.all()

    return Result(200, "获取网站类型列表成功", [k.to() for k in data])
