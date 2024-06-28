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


def download_image(url: str, j: int ):
    breed = url.split('/')[-2]
    breed_new = url.split('/')[-1].split('.')[0]
    path = os.getcwd() + '/Dogs'
    try:

        response = requests.get(url)
        status = response.status_code
        if status == 200:
            image = response.content
            if not os.path.isdir(breed):
                os.mkdir(path)
                os.mkdir(path + f"\\{breed}")
                with open(path + f"\\{breed}" + f"\\{breed}_{breed_new}_{j}.jpg", 'wb+') as file:
                    file.write(image)

        else:
            print('Не могу скачать картинку!')
    except Exception as error:
        print(error)
    # print(f"Загружена {j} картинка из {count_image}")


URL = "https://dog.ceo/api/breeds/image/random"

count_image = 5
counter = []
for j in tqdm(range(1, count_image + 1), colour='green'):
    uri_image = get_image_url(URL)
    if uri_image is not None:
        a = download_image(uri_image, j)
        counter.append(a)
    else:
        print('Error')

result = [x for x in counter if x is not None]

s = set(result)
for i in s:
    print(f"Порода '{i}': повторяется в загруженных фотографиях {result.count(i)} раз(а)")
