import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
headers = {"User-Agent": user_agent}

url = "https://hh.ru"
response = requests.get(url, headers=headers)
print(response.text)
print(response.status_code)
