import requests

cookies = {
    'showBlocks': 'all^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1',
    '__ddg1_': 'nD5thumwdI0zaf2aKWJY',
    '_ym_uid': '171873570187058743',
    '_ym_d': '1718736693',
    '_ga': 'GA1.2.1342777401.1718735702',
    '_gid': 'GA1.2.1263516264.1718735702',
    '_ga_BVMY6KEFHL': 'GS1.1.1718735701.1.1.1718736663.60.0.0',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'user_city': '134',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'showBlocks=all^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1^%^2C1; __ddg1_=nD5thumwdI0zaf2aKWJY; _ym_uid=171873570187058743; _ym_d=1718736693; _ga=GA1.2.1342777401.1718735702; _gid=GA1.2.1263516264.1718735702; _ga_BVMY6KEFHL=GS1.1.1718735701.1.1.1718736663.60.0.0; _ym_isad=2; _ym_visorc=b; user_city=134',
}

response = requests.get('https://world-weather.ru/pogoda/russia/saint_petersburg/', cookies=cookies, headers=headers)
print(response.status_code, response.text)