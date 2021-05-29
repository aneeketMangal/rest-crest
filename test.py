import requests, json
import jsonify
BASE = "http://127.0.0.1:5000/"
data = {"likes":2981, "name": "AneeBoi", "views": 97401},


response = requests.get(BASE + "login/"+"dsfadfsa")
print(response.json())
BASE = "http://127.0.0.1:5000/send"

while(True):
    s = input()
    t = input()
    d ={"name":"dsfadfsa", "user":s, "message":t}
    # DD = json.stringify(d)
    response = requests.get(BASE, params=d)
    print(response.url)
    print(response.json())