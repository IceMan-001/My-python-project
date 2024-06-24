import time
date = input('Date (dd-mm-yyyy): ')
try:
    valid_date = time.strptime(date, '%d-%m-%Y')
except ValueError:
    print('Invalid date!')
