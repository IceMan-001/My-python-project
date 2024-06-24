from collections import namedtuple

# вариант дикт
# data_dict = {
#     'name': 'George',
#     'occupation': 'Egypt',
#     'birthday': None
# }

# # вариант через тёупл
# data_tuple = ('', '', None)

Person = namedtuple('Person', ('name', 'occupation', 'birthday'))
person1 = Person('George', 'Egypt', '1990-09-27T12:30:00.00000')
person2 = Person('Ivan', 'Russia', '1991-09-27T12:30:00.00000')

print(person1)

print(person2._asdict())
person2_dict = person2._asdict()
person2_dict['name'] = 'Dmitriy'
print(Person(**person2_dict))
# print(person1.name, person1.occupation)
# print(person1[0], person1[1], person1[2])
