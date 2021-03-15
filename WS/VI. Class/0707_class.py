class Car:
    count = 0
    #클래스 변수 : 클래스에 하나 존재함.
    #즉 이 클래스로 만든 모든 객체가 공유

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    @classmethod
    #클래스 함수
    def get_count(cls):
        return cls.count

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
print(Car.get_count())
print(c1.get_count())
print(c1.count)
print(Car.count)
