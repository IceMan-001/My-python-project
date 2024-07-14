import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL 
    )   
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts ( 
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT, 
        FOREIGN KEY (user_id) REFERENCES accounts (id)  
    )
""")
# Последней строчкой соединяем поле user_id c полем id
# Внешний ключ user_id ссылается на таблицу accounts поле id
'''
пользователь с id=1 разместил пост с id=4 и так далее
связь один ко многим
user     post
id=1     id=4
id=1     id=5
id=2     id=6
'''
# Первой создается родительская таблица
# data = [
#     ('Vova', '892185222'),
#     ('Ivan', '896233333'),
#     ('Elena', '896233333')
# ]
# cursor.executemany('''
#     INSERT INTO accounts (name, phone)
#     VALUES (?, ?)
# ''', data)


# Очистить таблицу полностью
# cursor.execute("""
#     DELETE FROM accounts
# """)

# posts = [
#     (1, 'post_1', 'text for post_1'),
#     (1, 'post_2', 'text for post_2'),
#     (2, 'post_1 new', 'text for post_1_new'),
#     (2, 'post_2 new', 'text for post_2_new'),
#     (3, 'my post_1', 'text for new post'),
#     (3, 'my post_2', 'text for new post'),
# ]
# cursor.executemany('''
#     INSERT INTO posts (user_id, title, content)
#     VALUES (?, ?, ?)
# ''', posts)

# conn.commit()

# Получение данных из нескольких таблиц
cursor.execute('''
    SELECT accounts.name, posts.title, posts.content
    FROM accounts
    JOIN posts ON accounts.id = posts.user_id
''')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
