import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import csv
import menu
from datetime import datetime
import time


class Parser:
    def __init__(self):
        self.html = None
        self.soup = None
        self.data = None

    def get_html(self, url: str):
        user_agent = UserAgent()
        headers = {"User-Agent": user_agent.random}
        response = requests.get(url, headers=headers)
        self.html = response.text

    def get_data(self):
        self.soup = bs(self.html, 'html.parser')
        table = self.soup.find('table', class_="js_sortable")

        rows = table.find_all('tr')
        courser_info = {}
        for row in rows[2:]:
            if 'id' in row.attrs:
                continue
            else:
                number_code = row.find('td', class_='t-center').text.split()[0]
                literal_code = row.find('td', class_="t-center").text.split()[1]
                name = row.find('td', class_='t-left').text.split('\n')[0]
                course = row.find('td', class_='t-right').text.strip('\n')

                courser_info[literal_code] = {
                    "number_code": number_code,
                    "name": name,
                    "course": course
                }

        self.data = courser_info

    def print_data(self):
        for item in self.data.items():
            print(item)

    def betray_in_file(self):  # запись в файл txt
        with open('text.txt', 'w', encoding='utf-8') as file:
            for key, value in self.data.items():
                file.write(f'{key}, {value}\n')
        print('\n Файл записан! \n')

    def get_in_file(self):  # чтение из файла txt
        with open('text.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        print(data)
        print('Файл прочитан!')

    def betray_in_csv(self):  # запись в файл csw
        with open('text_w.csw', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for line in self.data.items():
                writer.writerow(line)
        print('Файл записан! \n')

    def get_from_csv(self):
        with open('text_w.csw', 'r', encoding='utf-8') as file:
            data = csv.reader(file)
            for row in data:
                print(*row)
        print('Файл прочитан!')

    def get_currency_data_search(self):
        today_s_date = soup.find('h2', class_="h2 blue").text.split()[3]
        course = (input('Введите искомую валюту: ').upper().strip())
        for key, value in self.data.items():
            if course not in self.data:
                print(f"Значение валюты не найдено в списке. \n"
                      f"Список доступных валют: {', '.join([currency for currency in self.data])}")
                break
            elif course == key:
                print(f"Для введенной валюты {course}  на {today_s_date} курс составляет: {value['course']}")

def date_selection():
    user_data = input('Введите интересующею дату в формате \033[3m\033[32m 2024-06-23 \033[0m: ')
    try:
        time.strptime(user_data, '%Y-%m-%d')
        url = f"https://www.alta.ru/currency/{user_data}/"
        return url
    except ValueError:
        print(f"Выведена не корректная дата. Курс валют будет выведен на {datetime.now().date()}")
        return f"https://www.alta.ru/currency/{datetime.now().date()}/"


def go():
    url = date_selection()
    courser_parser = Parser()
    courser_parser.get_html(url)
    courser_parser.get_data()
    the_choice = int(input(menu.MENU))
    if the_choice == 1:
        return courser_parser.print_data()
    elif the_choice == 2:
        return courser_parser.betray_in_file()
    elif the_choice == 3:
        return courser_parser.betray_in_csv()
    elif the_choice == 4:
        return courser_parser.get_in_file()
    elif the_choice == 5:
        return courser_parser.get_from_csv()
    elif the_choice == 6:
        return courser_parser.get_currency_data_search()


go()

# courser_parser.print_data()
# courser_parser.betray_in_file()
# courser_parser.get_in_file()
# courser_parser.betray_in_csv()
# courser_parser.get_from_csv()
# courser_parser.get_currency_data_search()
