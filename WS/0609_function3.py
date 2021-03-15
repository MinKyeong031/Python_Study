#수학
print(abs(-10))
print(round(7.264))
print(round(7.264, 1))
print(round(7.264, 2))
print(round(7.264, 3))
print(pow(2, 3))
print(min([10, -2, 3, 5]))
print(min(10, -2, 3, 5))
print(max([10, -2, 3, 5]))
print(max(10, -2, 3, 5))
print(sum([10, -2, 3, 5]))
#print(sum(10, -2, 3, 5)) -> 불가능
print(bin(255))
print(oct(255))
print(hex(255))

#자료형
import random
print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.choice(["종아", "지영", "민정"]))
s =  random.sample(["지윤", "솔민", "지안"], 2)
print(s)
print(random.sample(range(1, 45 + 1), 6))
반1 = ["현서", "수현", "나윤", "수연", "잎새", "진진"]
random.shuffle(반1)
print(반1)
c = list(range(1, 18 + 1))
random.shuffle(c)
print(c)
print(c[:5])