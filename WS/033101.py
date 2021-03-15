#연산자
a = 1 + 3
a = 2 ** 3 # ** : 제곱
print(a)
a = 3/2
print(a)
a = 3 % 2
print(a)
a = 5 % 3
print(a)
a += 1
a *= 2
# a++는 없음
print(True and False)
print(False or False)
print(not True)
print(not False)
print(not 1 != 1)

#in, not in() : 포함 관계를 조사하는 연산자
li = [1, 2, 3, 4]
print(1 in li)
print(5 in li)
print(5 not in li)
print(not (5 in li))
print("a" in "asdf")
print("Hell" in "Hello")
dic = {"name" : "John"}
print("name" in dic)
print("age" in dic)


#입력
#a = input() #콘솔로 부터 입력 받기, 자바스캐너 nextInt(), nextLine()
#print(a)
#name = input("당신의 이름은 ? ") #input을 통해 입력 받는 값의 타입 : 문자열
#print(name)
# 두 숫자를 입력받아 더하는 프로그램 작성
#num1 = int(input("숫자 입력 : ")) #콘솔로 부터 입력 받기, 자바스캐너 nextInt(), nextLine()
#print(num1)
#num2 = int(input("숫자 입력 : ")) #input을 통해 입력 받는 값의 타입 : 문자열
#print(num2)
#result = num1 + num2
#print(result)


#리스트
mylist1 = [1, 2, 3, 4, 5]
mylist2 = [1, 2.0, "Hello"]
print(mylist1)
person = ['김철수', 20, 171.3, True]
print(person[0])
print(person[1])
print(person[-2]) #뒤에서 두번째
print(person[-1])

#슬라이싱
l = mylist1[0:2]
print(l)
l = mylist1[0:3]
print(l)
print(mylist1[3:])
print(mylist1[-3:-1])
print(mylist1[-4:])
print("Hello"[0:2])
r1 = list(range(0, 10)) # 범위는 0~9
r2 = list(range(1, 11)) # 범위는 1~10
print(r1)
print(r2)


#튜플 -> 불변자료형
t1 = 1, 1.23, "Hello"
t2 = (1, 1.23, "Hello")
print(type(t1))
print(t1)

#불변자료형
#t1[0] =2 -> 불가능
#print(t1)
person = ("김철수", 20, 171.3)
print(person)
#언팩킹
name, age, height = person
print(person)
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
a, b, c = "abc"
print(a)
print(b)
print(c)
#n, a = person -> X
_, _, h = person
print(h)
t = (1)
print(type(t))
t = (1, )
print(type(t))


#딕셔너리 ->  키와 값 형식으로 데이터 저장
d1 = {}
person = {}
person["name"] = "김민경"
person["age"] = 18
print(person)
print(person["name"])
d2 = {"a" : "Hello", 1 : 1000, () : [1, 2, 3], (1, 2) : "3, 4"}
print(d2)
print(d2["a"])
print(d2[1])
print(d2[()])
print(d2[(1, 2)])
d3 = {'abc' : 123, 'def' : 456}
print(d3)
d3['abc'] = 789
print(d3)


#집합 -> 순서 X, 중복으로 저장 X
s1 = {1, 2, 3}
s2 = {2, 3, 4, 4} # {2, 3, 4}
s3 = {} #타입 : 딕셔너리
s3 = set()
print(s1)
print(s2)
print(s3)
s2.add(4) #무시
s2.add(5)
s2.add(5) #무시
print(s2) #{2, 3, 4, 5}

#합집합
print(s1.union(s2))
#교집합
print(s1.intersection(s2))
#차집합
print(s1.difference(s2))


#if문
'''
if 조건식:
    조건식이 참일 경우 수행할 문장
'''
if 1 + 1 == 2:
    print("True")
    if 2 + 2 == 5:
        print("False")

if True:
    print("True")

if 1 == 1 and 2 > 1:
    print("True (1 == 1 and 2 > 1)")