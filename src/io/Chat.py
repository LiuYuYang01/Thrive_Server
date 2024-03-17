from flask_socketio import emit, join_room

from src import socketio
from src.model import db
from src.model.ChatModel import ChatModel

# 当前房间号
thisRoom = 10001


# 加入房间
@socketio.on('joinRoom')
def joinRoom(room):
    global thisRoom

    thisRoom = room

    join_room(room)


# 在房间中发送消息
@socketio.on('roomMsg')
def roomMsg(data):
    # 将聊天内容保存到数据库
    chat = ChatModel(room=thisRoom, data=data)
    db.session.add(chat)
    db.session.commit()

    emit('roomMsg', data, room=thisRoom)
