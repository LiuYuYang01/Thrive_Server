from flask import Blueprint, request

from src.model import db
from src.model.CommentModel import CommentModel
from src import siwa
from src.siwadoc.CommentSiwa import CommentQuery, CommentBody, CommentBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

comment = Blueprint("comment", __name__)


# 新增评论
@comment.route("/comment", methods=["POST"])
@siwa.doc(tags=["评论管理"], summary="新增评论", description="新增评论记得把id去掉，否则可能会导致重复id异常",
          body=CommentBody)
def add():
    comment = request.json

    data = CommentModel(**comment)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除评论
@comment.route("/comment/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["评论管理"], summary="删除评论", description="通过ID删除指定评论")
def drop(id):
    data = CommentModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此评论")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除评论成功")


# 批量删除
@comment.route("/comment", methods=["DELETE"])
@siwa.doc(tags=["评论管理"], summary="批量删除评论", description="[1,2,3] 删除ID为1、2、3的数据", body=CommentBodyId)
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = CommentModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的评论")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除评论成功")


# 编辑评论
@comment.route("/comment", methods=["PATCH"])
@siwa.doc(tags=["评论管理"], summary="编辑评论", body=CommentBody)
def edit():
    comment = request.json

    data = CommentModel.query.filter_by(id=comment["id"]).update(comment)

    if not data:
        return Result(400, "编辑失败：没有此评论")

    db.session.commit()

    return Result(200, "编辑成功")


# 审核评论
@comment.route("/comment/audit/<int:id>", methods=["PATCH"])
def audit(id):
    data = CommentModel.query.filter(CommentModel.id == id).update({'audit': 1})

    if not data:
        return Result(400, "编辑失败：没有此评论")

    db.session.commit()

    return Result(200, "审核通过")


# 获取评论详情
@comment.route("/comment/<int:id>")
@siwa.doc(tags=["评论管理"], summary="获取评论详情", resp=CommentBody)
def get(id):
    data = CommentModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此评论")

    return Result(200, "获取评论详情成功", data.to())


# 获取评论列表
@comment.route("/comment")
@siwa.doc(tags=["评论管理"], summary="获取评论列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=CommentQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的评论在最前面排序
    paginate = CommentModel.query.order_by(CommentModel.crearetime.desc()).paginate(page=page, per_page=size,
                                                                                    error_out=False)

    data = {
        "result": [k.to() for k in paginate],
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取评论列表成功", data)
