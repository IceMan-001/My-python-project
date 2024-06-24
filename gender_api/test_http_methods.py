import requests
import json
from fake_useragent import UserAgent

user_agent = UserAgent()
# print(user_agent.random)  # user_agent.chrom

# Параметры запроса через & словарь 'args': {'age': '24', 'name': 'elena'}
# URL = 'http://httpbin.org/get?name=elena&age=24'
# response = requests.get(URL)
# # print(response.content)
# print(response.json())

# pip install fake-useragent  для подмены user agent


URL = 'http://httpbin.org/post'
headers = {'Content-Type': 'application/json'}
data = {'login': 'user', 'password': 'qwerty'}
response = requests.post(URL, json=json.dumps(data), headers=headers)
print(response.json())

print(data)
print(json.dumps(data))
print(type(data))
print(type(json.dumps(data)))

data_json = json.dumps(data)
data_dict = json.loads(data_json)
print(data_dict, type(data_dict))
