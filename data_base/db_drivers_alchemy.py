from sqlalchemy import create_engine, Integer, Column, ForeignKey, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///alchemy_drivers.db')

Base = declarative_base()


class Drivers(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    number = Column(Integer, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

driver_1 = Drivers(name='Dmitriy', phone=1111111111)
driver_2 = Drivers(name='Ivan', phone=2222222222)
driver_3 = Drivers(name='Elena', phone=3333333333)
driver_4 = Drivers(name='Yuri', phone=4444444444)

car_1 = Cars(user_id=1, brand='Mercedes-Benz', model='CLE', number='a222aa78')
car_2 = Cars(user_id=1, brand='Mercedes-Benz', model='CLA', number='b222bb78')
car_3 = Cars(user_id=2, brand='Audi', model='A1', number='c333cc78')
car_4 = Cars(user_id=2, brand='Audi', model='A3', number='d444dd78')
car_5 = Cars(user_id=3, brand='KIA', model='Ceed III', number='i555ii78')
car_6 = Cars(user_id=3, brand='KIA', model='K5', number='j666jj78')
car_7 = Cars(user_id=4, brand='Honda', model='Civic', number='s777ss78')
car_8 = Cars(user_id=4, brand='Honda', model='Accord', number='f888ff78')

# with Session() as session:
#     session.add_all([car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8])
#     session.commit()
#
# with Session() as session:
#     session.add_all([driver_1, driver_2, driver_3, driver_4])
#     session.commit()

with Session() as session:
    query = session.query(Drivers.name, Cars.brand, Cars.model).join(Cars, Drivers.id == Cars.user_id).all()

for item in query:
    print(f"The Driver \033[3m\033[32m{item[0]}\033[0m drives a brand car \033[3m\033[34m{item[1]} {item[2]}\033[0m")


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
