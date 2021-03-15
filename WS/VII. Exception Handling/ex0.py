#p211
#ZeroDivisionError
#print(10/0)

#NameError
#span = 10
#print(4 + span * 3)

#TypeError
#print('2' + 2)

list1 = [1, 2, 3]
#IndexError
#print(list1[2])
#print(list1[3])

try:
    print(list1[2]) #정상실행
    print(list1[3]) #예외발생
    print(list1[2]) #실행X
except:
    print("리스트의 요소에 접근하지 못했습니다.")
print("-" * 40)

f = open("file.txt", "w")
#f.write("Hello World")#정상실행
#f.write(str(100))#정상실행
try:
    f.write("Hello World")#정상실행
    f.write(100)#예외발생
except:
    print("타입 예외 발생(100은 쓸 수 없음)")
finally:
    print("예외 여부와 상관없이 무조건 실행")
    f.close()
print("-" * 40)

#p217
list2 = [1, 2, 3]
try:
    #print(list2[4]) #IndexError
    print(list2[0])
    print(list2[1])
    print(list2[2])
    print(list2[3])
except IndexError as e:
    print(e)
    print("예외발생")
else:
    print("성공적으로 모든 코드를 실행!")


















