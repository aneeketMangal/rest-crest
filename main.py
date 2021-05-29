from flask import Flask, render_template, request
from flask_socketio import SocketIO
import requests, json

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
currLoggedIn = ""
d = {}
@app.route('/login/<name>', methods = ['GET'])
def login(name):
    if(request.method == 'GET'):
        currLoggedIn = name
        if(name in d):
            dd = {"d": d, "cli": currLoggedIn}
            return dd
        else:
            d[name] = []
            dd = {"d": d, "cli": currLoggedIn}
            return dd
        
@app.route('/send', methods = ['GET'])   
def send():
    request_data = request.args
    if(request_data):
        name = ''
        message = ''
        user = ''
        if('message' in request_data):
            message = request_data['message']
        if('name' in request_data):
            name = request_data['name']
        else:
            return 'BAD RESPONSE'
        if('user' in request_data):
            user = request_data['user']
        else:
            return 'BAD RESPONSE'

        d[name].append([user, message])
        return {"name": name,"user": user,"message": message, "D":str(d[name])}
        
    else:
        return {"error": "dfosnaopi"}



# @app.route('/')
# def sessions():
#     return render_template('session.html')

# @socketio.on('connect')
# def connect():
#     print("a client connected")

# @socketio.on('disconnect')
# def disconnect():
#     print('Client disconnected')

# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')

# @socketio.on('my event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my event: ' + str(json))
#     socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    app.run(debug=True)