from flask import Blueprint, request

from src.model import db
from src.model.CateModel import CateModel
from src import siwa
from src.siwadoc.CateSiwa import CateQuery, CateBody, CateBodyId
from src.utils.jwt import TokenRequired
from src.utils.response import Result

cate = Blueprint("cate", __name__)


# 新增分类
@cate.route("/cate", methods=["POST"])
@siwa.doc(tags=["分类管理"], summary="新增分类", description="新增分类记得把id去掉，否则可能会导致重复id异常",
          body=CateBody)
@TokenRequired
def add():
    cate = request.json

    data = CateModel(**cate)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除分类
@cate.route("/cate/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["分类管理"], summary="删除分类", description="通过ID删除指定分类")
@TokenRequired
def drop(id):
    data = CateModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此分类")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除分类成功")


# 批量删除
@cate.route("/cate", methods=["DELETE"])
@siwa.doc(tags=["分类管理"], summary="批量删除分类", description="[1,2,3] 删除ID为1、2、3的数据", body=CateBodyId)
@TokenRequired
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = CateModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的分类")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除分类成功")


# 编辑分类
@cate.route("/cate", methods=["PATCH"])
@siwa.doc(tags=["分类管理"], summary="编辑分类", body=CateBody)
@TokenRequired
def edit():
    cate = request.json

    data = CateModel.query.filter_by(id=cate["id"]).update(cate)
    print(data)
    if not data:
        return Result(400, "编辑失败：没有此分类")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取分类详情
@cate.route("/cate/<int:id>")
@siwa.doc(tags=["分类管理"], summary="获取分类详情", resp=CateBody)
def get(id):
    data = CateModel.query.filter_by(id=id).first().to()
    data['children'] = []

    if not data:
        return Result(400, "获取失败：没有此分类")

    list = [k.to() for k in CateModel.query.all()]

    # 查询该分类下的所有子分类
    for cate in list:
        if cate['level'] == id:
            data['children'].append(cate)

    # 如果为空, 就不让他显示children
    if len(data['children']) == 0:
        del data['children']

    return Result(200, "获取分类详情成功", data)


# 获取分类列表
@cate.route("/cate")
@siwa.doc(tags=["分类管理"], summary="获取分类列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=CateQuery)
@TokenRequired
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的分类在最前面排序
    paginate = CateModel.query.filter_by(level=0).paginate(page=page, per_page=size, error_out=False)
    list = CateModel.query.all()

    def tree(pid, data):
        children = []

        for cate in data:
            if cate['level'] == pid:
                cate['children'] = tree(cate['id'], data)

                # 如果为空, 就不让他显示children
                if len(cate['children']) == 0:
                    del cate['children']

                children.append(cate)

        return children

    data = {
        "result": tree(0, [k.to() for k in list]),
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取分类列表成功", data)
