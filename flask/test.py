import requests, json

BASE = "http://127.0.0.1:5000/"
data = [{"likes":2981, "name": "AneeBoi", "views": 97401},
{"likes":3412, "name": "boi", "views": 67882},
{"likes":203, "name": "mangal", "views": 90892},
]
for i in range(len(data)):
	response = requests.put(BASE + "video/"+str(i+5), data[i])

	# try:
	# 	response = response.text
	# 	data = json.loads(response)
	# 	print(data)
	# except json.JSONDecodeError as e:
	print(response.json())
# # response = requests.delete(BASE + "video/2")
# print(response)
# response = requests.delete(BASE + "video/7")
# print(response)
response = requests.patch(BASE+ "video/5", {"likes":789798787})
print(response.json())
response = requests.get(BASE + "video/5")
print(response.json())
# # print(*response)
