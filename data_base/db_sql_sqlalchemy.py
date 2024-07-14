from sqlalchemy import create_engine, Integer, Column, ForeignKey, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Создание объекта для Engine (движок) для SQLite и установка СУБД
# В объекте engine будет храниться соединение с базой данных
engine = create_engine('sqlite:///alchemy.db')

# Создание базового класса для декларативного определения моделей
# declarative_base импортируется из sqlalchemy.orm и создает класс
Base = declarative_base()


# Определение моделей для таблиц users и posts
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text)


# Создание таблиц в базе данных (если они не существуют)
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
# 'sessionmaker' функция, которая создает сессию
Session = sessionmaker(bind=engine)

# Создание объектов модели User
user_1 = User(name='Dima', age=25)
user_2 = User(name='Vova', age=32)
user_3 = User(name='Ivan', age=35)

# with Session() as session:
#     session.add(user_1)
#     session.commit()

# with Session() as session:
#     session.add_all([user_2, user_3])
#     session.commit()


post_1 = Post(user_id=1, title='First post', content='This is text for first post')
post_2 = Post(user_id=2, title='Second post', content='This is text for second post')
post_3 = Post(user_id=3, title='Third post', content='This is text for third post')

# with Session() as session:
#     session.add_all([post_1, post_2, post_3])
#     session.commit()

# with Session() as session:
#     # query = session.query(User.name, Post.title, Post.content)
#     query = session.query(User).all()
#
#
# for item in query:
#     print(item.name, item.age)  # Dima 25 Vova 32 Ivan 35

# with Session() as session:
#     # query = session.query(User.name, Post.title, Post.content)
#     query = session.query(User).first()
#
# print(query.name)  # Dima

# with Session() as session:
#     # query = session.query(User.name, Post.title, Post.content)
#     # основные элементы -> запрос, таблица, фильтр
#     query = session.query(User).filter(User.age > 30).all()
# # query - это список.
# print(query[-1].name)  # 0 -> Vova; -1 -> Ivan

with Session() as session:
    query = session.query(User.name, Post.title, Post.content).join(Post, User.id==Post.user_id).all()

for item in query:
    print(item)
