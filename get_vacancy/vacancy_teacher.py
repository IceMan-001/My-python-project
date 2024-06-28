import requests
import json

from random import sample
from datetime import datetime


def format_datetime(published_str: str) -> str:
    published_dt = datetime.strptime(published_str[:19], "%Y-%m-%dT%H:%M:%S")
    published_at = datetime.strftime(published_dt, "%d.%m.%Y %H:%M")
    return published_at


def get_vacancy(url: str, text: str, page: int = 0):
    """
    Параметры запроса (URL-параметры)
    page - номер страницы
    per_page - количество вакансий на странице
    text - текст, встречающийся в вакансии
    area - местоположение (1 - Москва, 2 - Санкт-Петербург)
    https://api.hh.ru/vacancies?per_page=100&page=1&text=python&area=2
    """
    headers = {
        "User-Agent": "api-test-agent"
    }

    params = {
        "page": page,
        "per_page": 100,
        "text": text,
        "area": 2
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data


def parse_vacancy(vacancy: dict):
    id = vacancy["id"]
    name = vacancy["name"]

    if vacancy["department"]:
        if vacancy["department"]["name"]:
            department = vacancy["department"]["name"]
        else:
            department = "Не указана"
    else:
        department = "Не указана"

    if vacancy['salary']:
        salary = {}
        if vacancy['salary']["from"]:
            salary["from"] = vacancy['salary']["from"]
        if vacancy['salary']["to"]:
            salary["to"] = vacancy['salary']["to"]
    else:
        salary = "Не указана"

    published_at = format_datetime(vacancy['published_at'])
    vacancy_url = vacancy['alternate_url']

    if vacancy["snippet"]:
        snippet = {}
        if vacancy["snippet"]["requirement"]:
            snippet['requirement'] = vacancy["snippet"]["requirement"]
        if vacancy["snippet"]["responsibility"]:
            snippet["responsibility"] = vacancy["snippet"]["responsibility"]
    else:
        snippet = "Не указано"

    if vacancy['employment']:
        employment = vacancy['employment']['name']
    else:
        employment = 'Не указано'

    info = {
        "id": id,
        "name": name,
        "salary": salary,
        "snippet": snippet,
        "published_at": published_at,
        "department": department,
        "vacancy_url": vacancy_url,
        "employment": employment
    }
    return info


URL = "https://api.hh.ru/vacancies"
data = get_vacancy(url=URL, text="python")
found = data["found"]
pages = data["pages"]

print(f"Найдено {found} вакансий")
print(f"Всего - {pages} страниц")

list_of_vacancies = data["items"]
# print(*list_of_vacancies, sep='\n')

for i in range(1, pages + 1):
    vacancies = get_vacancy(url=URL, text="python", page=i)
    list_of_vacancies += vacancies["items"]
    print(f"Обработана {i}-я страница из {pages}")

print(f"Обработано {len(list_of_vacancies)} вакансий")

random_vacancies = sample(list_of_vacancies, 3)
vacancies_info = []
for vacancy in random_vacancies:
    vacancies_info.append(parse_vacancy(vacancy))

print(*vacancies_info, sep='\n')

"""
ДОМАШНЕЕ ЗАДАНИЕ:
1. Реализовать функцию parse_vacancy_api(vacancy_id)
url_api = "https://api.hh.ru/vacancies/id"
Для каждой вакансии функция должна возвращать:
а) скиллы (key_skills)
б) ближайшее метро
в) professional_roles

2. Реализовать функционал данного скрипта в стиле ООП
class Parser
    def get_data
    def parse_data
    def write_file
    def write_to_csv

class Vacancy

"""