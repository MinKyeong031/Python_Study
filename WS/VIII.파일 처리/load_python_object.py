import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'이름 : {self.name}\n나이 : {self.age}'

file = open('person_data.bin', 'rb')
person = pickle.load(file)
file.close()
print(person)
print(person.name)
print(person.age)

with open('people_data.bin', 'rb') as file:
    p_list = pickle.load(file)

print(p_list)
for p in p_list:
    print(p)