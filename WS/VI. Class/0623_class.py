'''PYTHON의 클래스
class 클래스이름:
    클래스변수
    @classmethod-클래스함수
    def 클래스이름(cls, 매개변수):
        pass
    def __init__(self):
        pass
    def 메서드이름(self, 매개변수):
        print(self, 변수이름)

객체이름 = 클래스이름()
'''

#멤버변수 : 객체 안에서 다 쓸 수 있는 변수
#멤버함수 : 객체 안에서 다 쓸 수 있는 함수
#클래스변수 : 클래스 안에서 다 쓸 수 있는 변수
#클래스함수 : 클래스 안에서 다 쓸 수 있는 함수

# #p.195
# class Car:
#     def __init__(self, type, speed):
#         self.type = type
#         self.speed = speed
#
#     def move(self):
#         print(f'{self.type}가 {self.speed} 속도로 움직입니다.')
#
#     def speed_up(self, amount):
#         self.speed += amount
#
#     def speed_down(self, amount):
#         self.speed -= amount
#
#
# my_car = Car("스포츠카", 100)
# your_car = Car("트럭", 50)
#
# my_car.move()
# my_car.speed_up(20)
# my_car.move()
# my_car.speed_down(50)
# my_car.move()
# print(my_car.type)
#
# your_car.move()
# your_car.speed_up(20)
# your_car.move()
# your_car.speed_down(50)
# your_car.move()
#
# print(my_car)
# print(your_car)
# print(type(my_car))
# print(type(your_car))

