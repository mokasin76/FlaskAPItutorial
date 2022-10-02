from urllib import response
import requests


BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "How to make REST API", "likes": 10, "views": 1000},
    {"name": "Football match", "likes": 100, "views": 10000},
    {"name": "My first dance", "likes": 1, "views": 5}
]

for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", data[i])
    print(response.json())

input()
response = requests.patch(BASE + "video/1", {"views": 999})
print(response.json())