import requests
from tqdm import tqdm


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


def download_image(url: str, j: int):
    try:
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            image = response.content
            with open(f'image_{j}.jpg', 'wb') as file:
                file.write(image)
        else:
            print('Не могу скачать картинку!')
    except Exception as error:
        print(error)
    # print(f"Загружена {j} картинка из {count_image}")


URL = "https://dog.ceo/api/breeds/image/random"

count_image = 10
for j in tqdm(range(1, count_image + 1), colour='green'):
    uri_image = get_image_url(URL)
    if uri_image is not None:
        download_image(uri_image, j)
    else:
        print('Error')
