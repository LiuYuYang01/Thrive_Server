from flask import Blueprint, request

import jwt
from src import app
from src.model import db
from src.model.UserModel import UserModel
from src import siwa
from src.siwadoc.UserSiwa import UserQuery, LoginBody, UserBody, UserBodyId, UserAdminPass
from src.utils.jwt import TokenRequired
from src.utils.response import Result
from datetime import datetime, timedelta
from hashlib import md5

user = Blueprint("user", __name__)


# 用户登录
@user.route("/login", methods=["POST"])
@siwa.doc(tags=["用户管理"], summary="用户登录", body=LoginBody)
def login():
    user = request.json

    data = UserModel.query.filter_by(username=user["username"]).first().to()
    if not data: return Result(400, "登录失败：没有此用户")

    # 给密码加密后与数据库中的做对比
    user["password"] = md5(user["password"].encode()).hexdigest()

    if user["password"] != data["password"]: return Result(400, "登录失败：用户密码错误")

    # 加载配置信息
    expire = app.config["EXPIRE"]
    secretkey = app.config["SECRET_KEY"]
    algorithm = app.config["ALGORITHM"]

    payload = {
        "exp": datetime.utcnow() + timedelta(seconds=expire)
    }

    # 生成token
    token = jwt.encode(payload, secretkey, algorithm)

    # 不返回密码字段
    del data["password"]

    return Result(200, "登录成功", {"token": token, "user": data})


# 新增用户
@user.route("/user", methods=["POST"])
@siwa.doc(tags=["用户管理"], summary="新增用户", description="新增用户记得把id去掉，否则可能会导致重复id异常",
          body=UserBody)
@TokenRequired
def add():
    user = request.json

    # 密码加密处理
    user["password"] = md5(user["password"].encode()).hexdigest()

    data = UserModel(**user)

    db.session.add(data)
    db.session.commit()

    return Result(200, "新增成功")


# 删除用户
@user.route("/user/<int:id>", methods=["DELETE"])
@siwa.doc(tags=["用户管理"], summary="删除用户", description="通过ID删除指定用户")
@TokenRequired
def drop(id):
    data = UserModel.query.filter_by(id=id).first()

    if not data:
        return Result(400, "删除失败：没有此用户")

    db.session.delete(data)
    db.session.commit()

    return Result(200, "删除用户成功")


# 批量删除
@user.route("/user", methods=["DELETE"])
@siwa.doc(tags=["用户管理"], summary="批量删除用户", description="[5,2,3] 删除ID为1、2、3的数据", body=UserBodyId)
@TokenRequired
def dropBatch():
    ids = request.json["ids"]

    for id in ids:
        data = UserModel.query.filter_by(id=id).first()

        if not data:
            return Result(400, f"批量删除失败：没有ID：{id}的用户")

        db.session.delete(data)

    db.session.commit()

    return Result(200, "批量删除用户成功")


# 编辑用户
@user.route("/user", methods=["PATCH"])
@siwa.doc(tags=["用户管理"], summary="编辑用户", body=UserBody)
@TokenRequired
def edit():
    user = request.json

    # 密码加密处理
    user["password"] = md5(user["password"].encode()).hexdigest()

    data = UserModel.query.filter_by(id=user["id"]).update(user)

    if not data:
        return Result(400, "编辑失败：没有此用户")

    db.session.commit()

    return Result(200, "编辑成功")


# 获取用户详情
@user.route("/user/<int:id>")
@siwa.doc(tags=["用户管理"], summary="获取用户详情", resp=UserBody)
def get(id):
    data = UserModel.query.filter_by(id=id).first().to()

    if not data:
        return Result(400, "获取失败：没有此用户")

    # 不返回密码字段
    del data["password"]

    return Result(200, "获取用户详情成功", data)


# 获取用户列表
@user.route("/user")
@siwa.doc(tags=["用户管理"], summary="获取用户列表", description="不传参数表示从第1页开始 每页查询5条数据",
          query=UserQuery)
def list():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    # 最新发布的用户在最前面排序
    paginate = UserModel.query.order_by(UserModel.createtime.desc()).paginate(page=page, per_page=size,
                                                                              error_out=False)

    result = [k.to() for k in paginate]

    # 删除所有的密码字段
    for data in result:
        del data["password"]

    data = {
        "result": result,
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取用户列表成功", data)


# 修改管理员密码
@user.route("/user/admin", methods=["PATCH"])
@siwa.doc(tags=["用户管理"], summary="修改管理员密码", body=UserAdminPass)
@TokenRequired
def editAdminPass():
    user = request.json

    # 查找管理员账号是否存在
    data = UserModel.query.filter_by(username=user["username"]).first()

    if not data:
        return Result(400, "编辑失败：没有此用户")

    # 密码加密处理
    user["oldPassword"] = md5(user["oldPassword"].encode()).hexdigest()

    # 判断旧密码是否正确
    if user["oldPassword"] == data.password:
        data.password = md5(user["newPassword"].encode()).hexdigest()
        db.session.commit()

        return Result(200, "编辑成功")
    else:
        return Result(400, "编辑失败：旧密码不正确，请重新输入")
