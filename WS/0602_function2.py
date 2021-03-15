#람다함수(익명함수)
double = lambda x : x * 2
add = lambda x, y: x + y
bigger = lambda x, y: x if x > y else y
make_list = lambda x, y: list(range(x, y))

print(double(3))
print(bigger(2, 8))

def return_lambda_func(prefix = ""):
    return lambda target: print(prefix, target)

a = return_lambda_func("Hello")
a("김민경")

print(max(3, 2))
print((lambda x,y: x if x > y else y)(3,2))

#p.8 factorial
def factorial(number):
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(4))

#repeat
def repeat(f, times = 1):
    for i in range(times):
        f()

repeat(lambda : print(factorial(5)), 3)
print("-" * 100)

#map
result = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(result)

result2 = [x * 2 for x in [1, 2, 3, 4]]
print(result2)

def square(x):
    return x * x

result = list(map(square, [1, 2, 3, 4]))
print(result)

#filter
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(result)

#reduce : 줄이다
from functools import reduce
s = reduce(lambda x, y: x + y, [1, 2, 3, 4])
p = reduce(lambda x, y: x * y, [1, 2, 3, 4])
r = reduce(lambda x, y: x + " " + y, ["Hello", "World", "Python"])
print(s)
print(p)
print(r)