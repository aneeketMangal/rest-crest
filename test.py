import requests, json
import jsonify
import time

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "login/"+"tempUser")
print(response.json())


dd = {}

    
while(True):
    s = input()
    t = input()
    BASE = "http://127.0.0.1:5000/send"
    d ={"name":"tempUser", "user":s, "message":t}
    response = requests.get(BASE, params=d)
    # print(response.url)
    print(response.json())
    d = {"name":"tempUser"}
    BASE = "http://127.0.0.1:5000/recieve"
    response = requests.get(BASE, params=d)
    # print(response.url)
    print(response.json())
    
threading.Thread(target=a).start()
threading.Thread(target=b).start()