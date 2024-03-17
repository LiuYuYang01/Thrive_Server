from flask import Blueprint, request

from src.model.ChatModel import ChatModel
from src.utils.jwt import TokenRequired
from src.utils.response import Result

chat = Blueprint("chat", __name__)


# 获取指定房间内的聊天记录
@chat.route("/chat/<int:room>")
def list(room):
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)

    paginate = ChatModel.query.filter_by(room=room).paginate(page=page, per_page=size, error_out=False)

    data = {
        "result": [k.to() for k in paginate],
        "page": paginate.page,
        "size": paginate.per_page,
        "pages": paginate.pages,
        "total": paginate.total,
        "prev": paginate.has_prev,
        "next": paginate.has_next
    }

    return Result(200, "获取房间聊天记录成功", data)


# 获取指定房间内的所有聊天记录
@chat.route("/chat/list/<int:room>")
def get(room):
    data = ChatModel.query.filter_by(room=room).all()

    if not data:
        return Result(400, "获取失败：没有此房间")

    return Result(200, "获取房间聊天记录成功", [k.to() for k in data])
