import requests
import bleach
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


def parse_vacancy(vacancy: dict, checklist: list):
    id = vacancy["id"]
    name = vacancy["name"]

    list_key_skills = ''
    for i in range(len(num_id["key_skills"])):
        if vacancy["key_skills"]:
            if vacancy["key_skills"][i]["name"]:
                list_key_skills += vacancy["key_skills"][i]["name"] + ', '
            else:
                list_key_skills = "Не указана"

    if vacancy["professional_roles"]:
        if vacancy["professional_roles"][0]['id']:
            professional_roles_id = vacancy["professional_roles"][0]['id']
        else:
            professional_roles_id = "Не указана"

    if vacancy["professional_roles"]:
        if vacancy["professional_roles"][0]['name']:
            professional_roles_name = vacancy["professional_roles"][0]['name']
        else:
            professional_roles_name = "Не указано"

    if vacancy["description"]:
        description = vacancy["description"]
        phrase = (bleach.clean(description, tags=[], strip=True))  # убираю теги из текста
        lst_metro = ''
        for metro_station in checklist:
            if metro_station in phrase:
                lst_metro += metro_station + ", "
        if len(lst_metro) == 0:
            lst_metro = "Не указана"

        info = {
            "id": id,
            "name": name,
            "key_skills": list_key_skills,
            "professional_roles_id": professional_roles_id,
            "professional_roles_name": professional_roles_name,
            "metro": lst_metro,
        }

        return info


url_api = "https://api.hh.ru/vacancies/"

list_id = [101282318, 91858609, 100632282, 100072226, 98562325,
           100749972, 100831655, 98524154, 99581179, 101824013,
           102076820]

if __name__ == '__main__':
    for x in list_id:
        num_id = parse_vacancy_api(x)
        print(parse_vacancy(num_id, list_metro.Check_list))
