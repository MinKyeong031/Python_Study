def cho(age):
    longa = age//10
    shorta = age%10
    blank = (age//2-(longa+shorta))//2
    print(f'긴 초 {longa}개. 짧은 초 {shorta}개를 준비했습니다!')
    print(' ' * blank + '*'*longa)
    print(' ' * blank + '|'*longa + '*'*shorta)
    print(' ' * blank + '|'*(longa+shorta))
    print('-'*(age//2))
    print('|' + ' ' * (age//2-2) + '|')
    print('|' + ' ' * (age//2-2) + '|')
    print('|' + ' ' * (age//2-2) + '|')
    print('-'*(age//2))

def punch(age):
    for i in range(0, age//10):
        print('퍽\t'*10)
    print('퍽\t' * (age%10))
    print(f'총 {age}대 때렸습니다.')

print("친구의 이름은?")
name = input()
print(f"{name}의 나이는?")
age = int(input())

cho(age)
print(f"{name}, 생일축하해!!")
punch(age)