import requests
import bleach
import csv
import os
import list_metro

"""1. Реализовать функцию parse_vacancy_api(vacancy_id)
url_api = "https://api.hh.ru/vacancies/id"
Для каждой вакансии функция должна возвращать:
а) скиллы (key_skills)
б) ближайшее метро
в) professional_roles"""


def parse_vacancy_api(number_id: int):
    headers = {"User-Agent": "api-test-agent"}
    params = {"id": number_id}

    vacancy_id = f"https://api.hh.ru/vacancies/{number_id}"

    response = requests.get(vacancy_id, params=params, headers=headers)
    data = response.json()
    return data


def parse_vacancy(vacancy_in_python: dict, checklist: list, metro_station=None, lst_metro=None,
                  professional_roles_name=None, professional_roles_id=None) -> dict:
    id = vacancy_in_python["id"]
    name = vacancy_in_python["name"]

    list_key_skills = ''
    for i in range(len(num_id["key_skills"])):
        if vacancy_in_python["key_skills"]:
            if vacancy_in_python["key_skills"][i]["name"]:
                list_key_skills += vacancy_in_python["key_skills"][i]["name"] + ', '
            else:
                list_key_skills = "Не указана"

    if vacancy_in_python["professional_roles"]:
        if vacancy_in_python["professional_roles"][0]['id']:
            professional_roles_id = vacancy_in_python["professional_roles"][0]['id']
        else:
            professional_roles_id = "Не указана"

    if vacancy_in_python["professional_roles"]:
        if vacancy_in_python["professional_roles"][0]['name']:
            professional_roles_name = vacancy_in_python["professional_roles"][0]['name']
        else:
            professional_roles_name = "Не указано"

    if vacancy_in_python["description"]:
        description = vacancy_in_python["description"]
        phrase = (bleach.clean(description, tags=[], strip=True))  # убираю теги из текста
        lst_metro = ''
        for metro_station in checklist:
            if metro_station in phrase:
                lst_metro += metro_station + ", "
        if len(lst_metro) == 0:
            lst_metro = "Не указана"

    if vacancy_in_python['address']:
        if not vacancy_in_python['address']['metro_stations']:
            metro_station = "Не указано"
        elif vacancy_in_python['address']['metro']['station_name']:
            metro_station = vacancy_in_python['address']['metro']['station_name']

    info = {
        "id": id,
        "name": name,
        "key_skills": list_key_skills,
        "professional_roles_id": professional_roles_id,
        "professional_roles_name": professional_roles_name,
        "metro_description": lst_metro,
        "metro": metro_station,
    }

    return info


url_api = "https://api.hh.ru/vacancies/"

list_id = [101282318, 91858609, 100632282, 100072226, 98562325,
           100749972, 100831655, 98524154, 99581179, 101824013,
           102076820]


def save_in_csv(vacancy_in_python: list, path_to_file: str, path_to_the_report_folder: str):  # Запись в файл csv
    if os.path.isdir(path_to_the_report_folder):
        with open(path_to_file, 'w'):
            pass
    if not os.path.isdir(path_to_the_report_folder):
        os.mkdir(path_to_the_report_folder)
    field_names = ['id', 'name', 'key_skills', 'professional_roles_id', 'professional_roles_name',
                   'metro_description', 'metro']

    with open(path_to_file, 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(vacancy_in_python)


if __name__ == '__main__':
    vacancy = []
    for value_dict in list_id:
        num_id = parse_vacancy_api(value_dict)
        answer = parse_vacancy(num_id, list_metro.Check_list)
        vacancy.append(answer)
        print(answer)

    save_in_csv(vacancy_in_python=vacancy, path_to_file='result/answer.csv', path_to_the_report_folder='result')
    print("\N{smiling face with sunglasses}""\N{smiling face with sunglasses}""\N{smiling face with sunglasses}")
