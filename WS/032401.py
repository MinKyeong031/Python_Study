a = 100
b = 1.234
c = "Hello"
d = 'World'
e1 = "I'm here"
e2 = 'Tom said "Hello"'
e3 = 'I\'m here'
b1 = True
b2 = False
d, e = "d", 2

f = float(100)
i = int(10.234)
s= str(2345)
print(f)
print(i)
print(s)

f = 1234
print(str(f) + "haha")

print(type(f)) #type(확인하고 싶은 값)
print(type(1.234))
print(type("Hello"))

print(isinstance(100,int)) #isinstance(확인하고 싶은 값, 타입)
print(isinstance(1.234,float))
print(isinstance("Hello",str))

print(1, 2, 3)
print(1, "b", "2.34")
print("Hello", end = "!") #원래 마지막에 들어가는 엔터 대신 !이 들어감
print("2020", "01", "01", sep = "-") #seperator : 분리자

print("*", end = "")
print("*", end = "")
print("*", end = "")
print("*", end = "")
print("*")
print("*" * 5)

#주석
"""
주석
"""
'''
주석
'''
s = "안녕"\
    "하세요."
s2 = """안녕하세용.
저는 누굴까용.
반가워용."""
print(s)
print(s2)

a = [1, 2, 3]
b = a
print(id(a)) #id()->식별자를 구하는 것
print(id(b))
print(a is b)
print(a == b)
#파이썬(자바) => is(==) : 객체 참조 비교_값 비교, .==(equals) = 동등성 비교_주소값 비교
b = [1, 2, 3]
print(a is b)
print(a == b)
b = [1, 4, 3]
print(a is b)
print(a == b)

a = "World"
b = 1000
c = 1.234
s = "Hello, %s, %d, %f" % (a, b, c)
print(s)
s = "Hello, {}, {}, {}".format(a, b, c)
print(s)
s = "Hello, {0}, {2}, {1}".format(a, b, c)
print(s)
s = f"Hello, {a}, {b}, {c}" #f = format
print(s)
s = "Hello, +{},| {}. {}".format(a, b, c)
print(s)
s = f"{1+2} {'Hello'.upper()} {','.join(['a', 'b', 'c'])}"
print(s)

bi = 0b11111111
print(bi)
bi = 0b1111_1111
print(bi)
bi = 0b1111_1111_1111_1111
print(bi)

h = 0xFF
print(h)
h = 0xFF_FF
print(h)

a = 10e1
print(a)
a = 10e2
print(a)
a = 10e-1
print(a)
a = 10e-2
print(a)

