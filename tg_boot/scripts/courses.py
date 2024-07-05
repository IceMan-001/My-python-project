import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class Parser:
    def __init__(self):
        self.url = "https://www.alta.ru/currency"
        self.html = None
        self.soup = None
        self.data = None

        self.get_html()
        self.get_data()

    def get_html(self):
        user_agent = UserAgent()
        headers = {"User-Agent": user_agent.random}
        response = requests.get(self.url, headers=headers)
        self.html = response.text

    def get_data(self):
        self.soup = bs(self.html, 'html.parser')
        table = self.soup.find('table', class_="js_sortable")
        rows = table.find_all('tr')

        courses_info = {}
        for row in rows[2:]:
            if 'id' in row.attrs:
                continue
            else:
                number_code = row.find('td', class_='t-center').text.split()[0]
                literal_code = row.find('td', class_='t-center').text.split()[1]
                name = row.find('td', class_='t-left').text.split('\n')[0]
                course = row.find('td', class_='t-right').text.strip('\n')

                courses_info[literal_code] = {
                    "number_code": number_code,
                    "name": name,
                    "course": course
                }

        self.data = courses_info
        return self.data

    def print_data(self):
        for item in self.data.items():
            print(item)

    def write_to_csv(self):
        pass

    def get_data_from_csv(self):
        pass

    def write_to_file(self):
        pass

    def get_from_file(self):
        pass


