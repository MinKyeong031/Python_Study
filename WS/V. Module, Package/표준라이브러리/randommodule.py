import random #174쪽 굉장히 중요

print(f'random.random() : {random.random()}')
print(f'0~9 : random.random() : {int(random.random()*10)}')
print(f'1~10 : random.random() : {int(random.random()*10)+1}')
print(f'1~10 : random.random() : {int(random.random()*10)%3}')

print(random.uniform(2.5, 10.0))
print(f'0~9 정수 : {random.randrange(9+1)}')
print(f'1~10 정수 : {random.randrange(1, 10+1)}')
print(f'1~10 홀수 : {random.randrange(1, 10+1, 2)}')
print(f'1~10 정수 : {random.randint(1, 10)}')

foods = ['떡볶이', '족발', '연어', '샤브샤브']
print(f'오늘 뭐 먹을까? : {foods[random.randrange(4)]}')
print(f'오늘 뭐 먹을까? : {random.choice(foods)}')

반1 = list(range(1, 19+1))
반1.remove(5)
print(random.choice(반1))
print('before : ', 반1)
random.shuffle(반1)
print('after : ', 반1)
print(f'random.sample(반1, 5) : {random.sample(반1, 5)}')

print(f'이번 주 행운의 번호 : 두둥탁 : {random.sample(list(range(1, 45+1)), 6)}')