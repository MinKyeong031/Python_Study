class DeletableClass:
    def __del__(self):
        print("delete")

d = DeletableClass()
del d

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Person 설명, 이름은 {self.name}, 키는 {self.height}'

    def __len__(self):
        return self.height

    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'age':
            return self.age
        return None

p = Person("성수", 13, 154)
print(p)
print(len(p)) #__len__()
print(p['age']) #__getitem__('age')
print(p['name']) #__getitem__('name')