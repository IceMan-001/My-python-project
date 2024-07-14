import sqlite3

# Подключение к базе данных (если базы не существует, она будет создана автоматически)
# через метод connect из sqlite3 создать объект подключения из
conn = sqlite3.connect("example.db")

# Создание курсора для выполнения операций с базой данных (запросов)
cursor = conn.cursor()
# Выполнение двух строчек кода создает в рабочей директории файл с базой данных


# Создание таблицы (Чтобы создать таблицу у объекта cursor вызвать метод execute)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        age INTEGER
    )
""")

# Вставка данных
# cursor.execute("""
#      INSERT INTO users (name, lastname, age)
#      VALUES (? ,?, ?)
#  """, ('Dima', 'Ivanov', 30))  # кортеж с данными

# Сохранение изменения
# conn.commit()

# Добавление нескольких строк в таблицу
# создаем список кортежей
# data = [
#     ('Vova', 'Petrov', 30),
#     ('Ivan', 'Sidorov', 40),
#     ('Elena', 'Ivanona', 32)
# ]
# закомментирована, чтобы данные не добавлялись каждый раз при вызове программы
# cursor.executemany('''
#     INSERT INTO users (name, lastname, age)
#     VALUES (?, ?, ?)
# ''', data)

# Сохранение изменений
# conn.commit()

# Удаление данных
# cursor.execute('''
#     DELETE FROM users
#     WHERE age = 32
# ''')

cursor.execute('''
    UPDATE users
    SET name = 'Sasha'
    WHERE name = 'Dima'
''')

conn.commit()

# Получение данных (запрос)
cursor.execute('SELECT * FROM users')
# Получение строчек из объекта cursor
# Вызов у объекта cursor метода fetchall() -> выдает все строчки один раз и очищается
# (второй раз его использовать нельзя)
rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)
# # Закрытие курсора и соединения обязательно
cursor.close()
conn.close()





# cursor.execute("""
#     DELITE FROM users
#     WHERE ago = 30
# """)
#
# cursor.execute("""
#     UPDATE users
#     SET name 'Sasha'
#
# """)
# conn.commit()
