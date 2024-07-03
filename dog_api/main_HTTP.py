import requests
from tqdm import tqdm
import os


def get_image_url(url: str) -> str | None:  # строка либо пустой объект
    # отправка GET запроса на сервер
    try:
        response = requests.get(URL)
        status = response.status_code
        if status == 200:
            # получили тело ответа и преобразовали в json
            data = response.json()
            # получили ссылку на картинку из словаря
            url_image = data['message']
            return url_image
        else:
            return None
    except Exception as error:
        print(error)
        return None


def download_image(url: str):

    if not os.path.isdir('Dogs'):
        os.mkdir('Dogs')
    breed = url.split('/')[-2]
    breed_new = url.split('/')[-1].split('.')[0]
    try:
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            image = response.content
            if os.path.isdir(f"{'Dogs'}\\{breed}"):
                number = len(os.listdir(f"{'Dogs'}\\{breed}\\"))
                with open(f"{'Dogs'}\\{breed}\\{number + 1}. {breed}_{breed_new}.jpg", 'ab') as file:
                    file.write(image)
            if not os.path.isdir(f"{'Dogs'}\\{breed}"):
                os.mkdir(f"{'Dogs'}\\{breed}")
                with open(f"{'Dogs'}\\{breed}\\{1}. {breed}_{breed_new}.jpg", 'ab') as file:
                    file.write(image)
        else:
            print('Не могу скачать картинку!')
    except Exception as error:
        print(error)
    # print(f"Загружена {j} картинка из {count_image}")


def sort_go(path_to_file: str, path_to_the_report_folder: str):
    if os.path.isdir(path_to_the_report_folder):
        with open(path_to_file, 'w'):
            pass
    # Указываем путь к директории
    directory = "Dogs/"

    # Получаем список файлов
    files = os.listdir(directory)

    for name_of_breed in files:
        ln_lst = len(os.listdir(f"{directory}\\{name_of_breed}\\"))

        print(f"Порода \033[3m\033[32m'{name_of_breed}'\033[0m: повторяется в загруженных "
              f"фотографиях \033[3m\033[34m {ln_lst}\033[0m раз(а)")

        if not os.path.isdir(path_to_the_report_folder):
            os.mkdir(path_to_the_report_folder)

        with open(path_to_file, 'a', encoding='utf-8') as fail:
            fail.write(f"Порода {name_of_breed}: повторяется в загруженных "
                       f"фотографиях  {ln_lst} раз(а)\n")


URL = "https://dog.ceo/api/breeds/image/random"

count_image = int(input('\033[3m\033[36mВведите количество фотографий для загрузки: \033[0m'))
for j in tqdm(range(1, count_image + 1), colour='green'):
    uri_image = get_image_url(URL)
    if uri_image is not None:
        download_image(uri_image)
    else:
        print('Error')

sort_go(path_to_file='result/sort_answer.txt', path_to_the_report_folder='result')
print("\N{smiling face with sunglasses}""\N{smiling face with sunglasses}""\N{smiling face with sunglasses}")
