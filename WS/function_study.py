# def greet():
#     print("Hello")
#
# ret = greet()
# print(ret)

#def add(x, y):
#     """add two parameters"""
#     return x + y
#
# print(add(2, 3))
# print(add.__doc__)#"""글""" 출력

# def arithmetics(x, y):
#     return x + y, x - y, x * y, x / y # -> tuple
#
# result = arithmetics(10, 5)
# print(result)
# #tuple
# print(type(result))

# def arithmetics_return_list(x, y):
#     return [x + y, x - y, x * y, x / y]
#
# result = arithmetics_return_list(10, 5)
# # [15, 5, 50, 2.0] 출력
# print(result)
# print(type(result))

# def say_greet_msg(name, msg = "Hello"):
#     print(msg, name)
#
# say_greet_msg("김철수")
# say_greet_msg("김철수", "안녕")
# #keyword arguments 이용하여 값 전달
# say_greet_msg(name = "김철수")
# say_greet_msg(name = "김철수", msg = "안녕")
# #인자값이 정의된 순서대로 전달 안해도 OK
# say_greet_msg(msg = "안녕", name = "김철수")

# def make_list(*items, li = []):
#     for item in items:
#         li.append(item)
#     return li
#
# print(make_list(1, 2, 3))
# print(make_list(4, 5, 6)) #[4, 5, 6]이 아닌 [1, 2, 3, 4, 5, 6]을 반환함
# print(make_list(4, 5, 6, li = [])) #이렇게 사용하게 되면 디폴트값의 의미가 없음
#
# def make_list_fix(*items, li = None):
#     if li is None:
#         li = []
#     for item in items:
#         li.append(item)
#     return li
#
# print(make_list_fix(1, 2, 3))
# print(make_list_fix(4, 5, 6))

# def say_Greet_msgs(*names, msg = "Hello"):
#     #names 는 tuple
#     print(type(names))
#     for name in names:
#         print(msg, name)
#
# say_Greet_msgs("김철수", "이영희", "신구", "유미림", msg = "헬로~")

# def my_sum(*numbers):
#     s = 0
#     for n in numbers:
#         s += n
#     return s
#
# print(my_sum(1, 2, 3, 4))

# def my_func(*args, **kwargs): # * : 가변인자(튜플), ** : 키워드 가변인자(딕셔너리)
#     print(type(kwargs)) #dict
#     for a in args:
#         print(a)
#     for k, v in kwargs.items():
#         print("key : ", k, "values : ", v)
#
# my_func(1, 1.234, "Hello", a = 1234, b = "World")#앞에 3개는 튜플, 뒤에 2개는 딕셔너리
# #섞어서 쓰는 것은 불가능하다.
#
# t = (1, 1.234, "Hello")
# li = [1, 1.234, "Hello"]
# li2 = ["Hello"]
# d = {"a" : 1234, "b" : "World"}
#
# #starred expression 사용
# my_func(*t, **d)
# my_func(*li, **d)

# import builtins
# import types
# builtin_function_names = [name for name, obj in vars(builtins).items() if isinstance(obj, types.BuiltinFunctionType)]
# print(builtin_function_names)
# open = 200