"""Устанавливаем библиотеку для парсинга bs4"""
import requests
import json

from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_html(url: str) -> str | None:
    user_agent = UserAgent()
    headers = {"User-Agent": user_agent.random}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Код ответа {response.status_code}")
        status = response.status_code
        if status == 200:
            return response.text

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    print(response)


def get_weather(html: str):
    if html is None:
        return
    soup = bs(html, 'html.parser')
    # date = soup.find('div', class_="dates short-d").text.split(', ')  # None
    date = soup.find_all('div', class_="dates short-d")[1].text.split(', ')  # None
    # date = soup.find('div', class_="dates short-d red").text.split(', ')  # None

    day_of_week = date[0]
    day_of_month = date[1]

    table = soup.find('table', class_="weather-today short")
    rows = table.find_all('tr')
    weather_today = {"day_of_week": day_of_week,
                     "day_of_month": day_of_month
                     }
    for row in rows:
        weather_day = row.find('td', class_="weather-day").text
        temperature = row.find('td', class_="weather-temperature").text
        atmosphere = row.find('td', class_="weather-temperature").find('div').get('title')
        weather_feeling = row.find('td', class_="weather-feeling").text
        probability = row.find('td', class_="weather-probability").text
        pressure = row.find('td', class_="weather-pressure").text
        wind = row.find('td', class_='weather-wind').find_all('span')[0].get('title')
        wind_ms = row.find('td', class_='weather-wind').find_all('span', class_="tooltip")[1].text
        wind_kch = row.find('td', class_='weather-wind').find_all('span', class_="tooltip")[1].get('title')
        humidity = row.find('td', class_="weather-humidity").text

        weather_today[weather_day] = {
            "temperature": temperature,
            "atmosphere": atmosphere,
            "weather_feeling": weather_feeling,
            "probability": probability,
            "pressure": pressure,
            "wind": {
                "wind_direction": wind,
                "wind_ms": wind_ms,
                "wind_kch": wind_kch
            },
            "humidity": humidity
        }
    return weather_today


URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/"

html = get_html(URL)
weather_info = get_weather(html)

weather_json = json.dumps(weather_info, indent=2, ensure_ascii=False)
print(weather_json)

# with open('index.html', 'w') as file:
#     file.write(html)
