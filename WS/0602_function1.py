def func():
    print("func")

a = func

def func2(b):
    b()
    return b

result = func2(a)#실행
result()#실행