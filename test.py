import requests, json
import jsonify
import time

BASE = "http://anee.pythonanywhere.com/"

response = requests.get(BASE + "login/"+"tempUser")
print(response)
print(response.content)


dd = {}

    
while(True):
    s = input()
    t = input()
    BASE = "http://anee.pythonanywhere.co/send"
    d ={"name":"tempUser", "user":s, "message":t}
    response = requests.get(BASE, params=d)
    # print(response.url)
    print(response.json())
    d = {"name":"tempUser"}
    BASE = "http://anee.pythonanywhere.com/recieve"
    response = requests.get(BASE, params=d)
    # print(response.url)
    print(response.json())
    
threading.Thread(target=a).start()
threading.Thread(target=b).start()