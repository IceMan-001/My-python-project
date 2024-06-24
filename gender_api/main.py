import requests
from transliterate import translit


def get_gender(name: str):
    url = f"https://api.genderize.io/?name={name}"
    try:
        resource = requests.get(url)
    except Exception as err:
        print(err)
        resource = None
    if resource is not None:

        # print(resource.status_code)  # статус запроса 200
        # print(resource.json())  # результата запроса
        data = resource.json()
        if data['gender'] == 'female':
            gender = 'женский'
        elif data['gender'] == 'male':
            gender = 'мужской'
        else:
            gender = 'не определен'

        probability = data['probability']
        name = translit(value=name, language_code='ru', reversed=False)  # переводит имя с английского на русский

        result = f"Имя - {name}, пол - {gender}, вероятность - {probability * 100}%"
        print(result)
    else:
        print('Ошибка выполнения запроса!')


get_gender('Elena')
