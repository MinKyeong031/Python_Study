#가변 인자 : 인자의 개수가 변할 수 있음
def max_min(*num):
    # max_v = num[0]
    # min_v = num[0]
    # for n in num:
    #     if max_v < n:
    #         max_v = n
    #     if n < min_v:
    #         min_v = n
    # return max_v, min_v
    return max(num), min(num)
max_value, min_value = max_min(6, 2, 7, 8, 3, -7)
print(max_value, min_value) #8 -7
max_value, min_value = max_min(1, 9, 10, 0, -16)
print(max_value, min_value) #10 -16

#키워드 인자 : 인자에 이름이 붙어있음
# #인자 기본값 : =(초기화)
# def print_name_age(name, age = 18):
#     print("{}님은 {}살".format(name, age))
# print_name_age("권혜수") #권혜수님은 18살
# print_name_age("강종아", age = 17) #강종아님은 17살
# print_name_age("강종아", 17) #강종아님은 17살
# print_name_age(age = 17, name = "강종아") #강종아님은 17살
#
# #가변 키워드 인자 : 인자에 이름이 붙어있으면서 변할 수 있는 개수
# def say_hi(*names, hi = "안녕"):
#     for name in names:
#         print("{}님 {}~".format(name, hi))
#     return
# say_hi("김정아") #김정아님 안녕~\n
# say_hi("김정아", "김지영") #김정아님 안녕~\n 김지영님 안녕~\n
# say_hi("김정아", "김지영", hi = "니하오") #김정아님 니하오~\n김지영님 니하오~\n
# say_hi("김정아", "김지영", "니하오") #김정아님 니하오~\n김지영님 니하오~\n