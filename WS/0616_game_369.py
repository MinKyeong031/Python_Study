#369게임
#1~9까지 반복
#숫자에 3, 6, 9가 있는지 센다. -> count
#count == 0: 숫자 출력
#count == 1: "짝" 출력
#count == 2: "짝짝" 출력
#count == n: "짝"*n 출력
#count != 0: "짝"*count 출력

# #1
# def count369(i):
#     cnt = 0
#     if i % 10 == 3 or i % 10  == 6 or i % 10  == 9: #1의 자리
#         cnt += 1
#     if i // 10 == 3 or i // 10  == 6 or i // 10  == 9:#10의 자리
#         cnt += 1
#     return cnt

# #2
# def count369(i):
#     cnt = 0
#     i_string = str(i)
#     for ch in i_string:
#         if ch == "3" or ch == "6" or ch == "9":
#             cnt += 1
#     return cnt

# #3
# def count369(i):
#     cnt = 0
#     i_string = str(i)
#     for ch in i_string:
#         if ch in "369":
#             cnt += 1
#     return cnt

# #4
# def count369(i):
#     i_string = str(i)
#     return i_string.count('3') + i_string.count('6') + i_string.count('9')
#
# for i in range(1, 20 + 1):
#     count = count369(i)
#     if count == 0:
#         print(i)
#     else:
#         print("짝" * count)

#뿌쑝!
# #1
# def count369(i):
#     cnt = 0
#     i_string = str(i)
#     for ch in i_string:
#         if ch in "369":
#             cnt += 1
#     return cnt
#
# for i in range(1, 50 + 1):
#     if i % 5 == 0:
#         print("뿌쑝!")
#     else:
#         count = count369(i)
#         if count == 0:
#             print(i)
#         else:
#             print("짝" * count)

# #2
# def count369(i):
#     cnt = 0
#     i_string = str(i)
#     for ch in i_string:
#         if ch in "369":
#             cnt += 1
#     return cnt
#
# for i in range(1, 50 + 1):
#     count = count369(i)
#     if count != 0:
#         print("짝" * count)
#     else:
#         if i % 5 == 0:
#             print("뿌쑝!")
#         else:
#             print(i)