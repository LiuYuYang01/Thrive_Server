from src import socketio

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)