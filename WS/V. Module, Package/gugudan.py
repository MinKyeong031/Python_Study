#p.142
def gugudan(n):
    print(f'{n} 단을 출력합니다.')
    for i in range(1, 10):
        print(f'{n} x {i} = {n*i}')

if __name__ == '__main__':
    gugudan(3)
