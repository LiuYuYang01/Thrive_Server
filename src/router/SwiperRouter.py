from flask import Blueprint, request

from src.model import db
from src.model.SwiperModel import SwiperModel
from src import siwa
from src.siwadoc.SwiperSiwa import SwiperQuery, SwiperBody, SwiperBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

swiper = Blueprint("swiper", __name__)


# 新增轮播图
@swiper.route("/swiper", methods=["POST"])
@siwa.doc(tags=["轮播图管理"], summary="新增轮播图", description="新增轮播图记得把id去掉，否则可能会导致重复id异常",
          body=SwiperBody)
def add():
    swiper = request.json
    print(swiper)

    data = SwiperModel(**swiper)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除轮播图
@swiper.route("/swiper/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["轮播图管理"], summary="删除轮播图", description="通过ID删除指定轮播图")
def drop(id):
    data = SwiperModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此轮播图")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除轮播图成功")


# 批量删除
@swiper.route("/swiper", methods=["DELETE"])
@siwa.doc(tags=["轮播图管理"], summary="批量删除轮播图", description="[1,2,3] 删除ID为1、2、3的数据", body=SwiperBodyId)
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = SwiperModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的轮播图")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除轮播图成功")


# 编辑轮播图
@swiper.route("/swiper", methods=["PATCH"])
@siwa.doc(tags=["轮播图管理"], summary="编辑轮播图", body=SwiperBody)
def edit():
    swiper = request.json

    data = SwiperModel.query.filter_by(id=swiper["id"]).update(swiper)

    if not data:
        return Result(400, "编辑失败：没有此轮播图")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取轮播图详情
@swiper.route("/swiper/<int:id>")
@siwa.doc(tags=["轮播图管理"], summary="获取轮播图详情", resp=SwiperBody)
def get(id):
    data = SwiperModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "获取失败：没有此轮播图")

    return Result(200, "获取轮播图详情成功", data.to())


# 获取轮播图列表
@swiper.route("/swiper")
@siwa.doc(tags=["轮播图管理"], summary="获取轮播图列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=SwiperQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的轮播图在最前面排序
    paginate = SwiperModel.query.order_by(SwiperModel.crearetime.desc()).paginate(page=page, per_page=size,
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

    return Result(200, "获取轮播图列表成功", data)
