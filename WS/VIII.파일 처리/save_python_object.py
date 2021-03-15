import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'이름 : {self.name}\n나이 : {self.age}'

p = Person('일미림', 18)
p2 = Person('이미림', 28)
p3 = Person('삼미림', 20)
people = [p, p2, p3]
print(people)
for person in people:
    print(person)

file = open('person_data.bin', 'wb')
pickle.dump(p, file)
file.close()

with open('people_data.bin', 'wb') as file:
    pickle.dump(people, file)