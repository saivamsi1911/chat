 from flask import flask
 from flask_socketio import SocketIO, send

 app=FLask(__name__)
 app.config('SECRET KEY')='mysecret'
 socketio=SocketIO(app)

@socketio.on('mesasge')
def handleMessage(msg):
    printf('Message: '+msg)
    send(msg, broadcast=True)


if __name__='__main__':
    socketio.run(app)
