from flask import Flask,render_template
from flask_socketio import SocketIO, send

app=Flask(__name__,template_folder="templates")
app.config['SECRET KEY']='mysecret'
socketio=SocketIO(app)

@app.route("/")
def home():
    return render_template("chatroom.html")


@socketio.on('message')
def handleMessage(msg):
    print('Message: '+msg)
    send(msg, broadcast=True)


if __name__=='__main__':
    socketio.run(app)
