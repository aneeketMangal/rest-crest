from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '2498*&trw&23'
socketio = SocketIO(app)


@app.route("/")
def session():
	return render_template('session.html')


if __name__ == "__main__":
	socketio.run(app, debug = True)