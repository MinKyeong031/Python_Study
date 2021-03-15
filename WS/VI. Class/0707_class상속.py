class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        #print(self.name + "가 " + food + "를 먹습니다.")
        print(f'{self.name}가  {food}를 먹습니다.')

    def __str__(self):
        #return self.name + "는 " + str(self.age) + "살입니다."
        return f'{self.name}는 {self.age}살입니다.'


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) #*****
        self.salary = salary

    def work(self):
        print("열심히 일을 합니다.")

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

e = Employee("수연이", 18, 300)
print(e)
e.eat('낙지곱창새우')
e.work()
r = e.get_salary()
print(f'급료는 {r}만원입니다.')