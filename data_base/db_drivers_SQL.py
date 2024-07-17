import sqlite3

conn = sqlite3.connect("drivers.db")
cursor = conn.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS drivers(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         phone INTEGER NOT NULL
#         )
# """)
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         id INTEGER PRIMARY KEY,
#         driver_id  INTEGER NOT NULL,
#         brand TEXT NOT NULL,
#         model TEXT NOT NULL,
#         number INTEGER NOT NULL
#         )
# """)
#
# """
# driver   car
# id=1     d_id=1 Mercedes-Benz CLE a222aa78
#          d_id=1 Mercedes-Benz CLA b222bb78
# id=2     d_id=2 Audi A1 c333cc78
#          d_id=2 Audi A3 d444dd78
# id=3     d_id=3 KIA Ceed III i555ii78
#          d_id=3 KIA K5 j666jj78
# id=4     d_id=4 Honda Civic s777ss78
#          d_id=4 Honda Accord f888ff78
# """
#
# data = [
#     ('Dmitriy', '1111111111'),
#     ('Ivan', '2222222222'),
#     ('Elena', '3333333333'),
#     ('Yuri', '4444444444')
# ]
# cursor.executemany('''
#     INSERT INTO drivers (name, phone)
#     VALUES (?, ?)
# ''', data)
#
# cars = [
#     (1, 'Mercedes-Benz', 'CLE', 'a222aa78'),
#     (1, 'Mercedes-Benz', 'CLA', 'b222bb78'),
#     (2, 'Audi', 'A1', 'c333cc78'),
#     (2, 'Audi', 'A3', 'd444dd78'),
#     (3, 'KIA', 'Ceed III', 'i555ii78'),
#     (3, 'KIA', 'K5', 'j666jj78'),
#     (4, 'Honda', 'Civic', 's777ss78'),
#     (4, 'Honda', 'Accord', 'f888ff78'),
# ]
#
# cursor.executemany('''
#     INSERT INTO cars (driver_id, brand, model, number)
#     VALUES (?, ?, ?, ?)
# ''', cars)

# conn.commit()

cursor.execute('''
    SELECT drivers.name, cars.brand, cars.model
    FROM drivers
    JOIN cars ON drivers.id = cars.driver_id
''')
rows = cursor.fetchall()

for row in rows:
    print(f"The Driver {row[0]} drives a brand car {row[1]} {row[2]}")


cursor.close()
conn.close()

"""
The Driver Dmitriy drives a brand car Mercedes-Benz CLE
The Driver Dmitriy drives a brand car Mercedes-Benz CLA
The Driver Ivan drives a brand car Audi A1
The Driver Ivan drives a brand car Audi A3
The Driver Elena drives a brand car KIA Ceed III
The Driver Elena drives a brand car KIA K5
The Driver Yuri drives a brand car Honda Civic
The Driver Yuri drives a brand car Honda Accord
"""