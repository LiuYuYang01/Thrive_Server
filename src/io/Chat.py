from flask_socketio import emit, join_room

from src import socketio


@socketio.on('msg')
def handle_message(data):
    emit('msg', data, broadcast=True)  # 对所有房间传播


@socketio.on('room')
def joinRoom(data, room):
    join_room(room)

    emit('room', data, room=room)
