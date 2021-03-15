#주민등록번호로 생년월일, 성별, 출생 지역 알아내기
def PersonInfo(name, number):
    y = number[:2]
    m = number[2:4]
    d = number[4:6]
    g = int(number[7])
    rn = int(number[8:10])

    ret = f'{name}님의 주민등록번호는 {number}입니다.\n'
    ret += f'{name}님의 YY/MM/DD은 {y}/{m}/{d}입니다.\n'

    if (g % 2) == 0:
        ret += f'{name}님은 여자입니다.\n'
    else:
        ret += f'{name}님은 남자입니다.\n'

    if 0 <= rn <= 8:
        ret += f'{name}님의 출생 지역은 서울입니다.'
    elif 9 <= rn <= 12:
        ret += f'{name}님의 출생 지역은 부산입니다.'
    elif 13 <= rn <= 15:
        ret += f'{name}님의 출생 지역은 인천입니다.'
    elif 16 <= rn <= 25:
        ret += f'{name}님의 출생 지역은 경기입니다.'
    elif 26 <= rn <= 34:
        ret += f'{name}님의 출생 지역은 강원입니다.'
    elif 35 <= rn <= 47:
        ret += f'{name}님의 출생 지역은 충청입니다.'
    elif 48 <= rn <= 66:
        ret += f'{name}님의 출생 지역은 전라입니다.'
    elif 67 <= rn <= 91:
        ret += f'{name}님의 출생 지역은 경상입니다.'
    elif 92 <= rn <= 95:
        ret += f'{name}님의 출생 지역은 제주입니다.'
    return ret


p1 = PersonInfo("김민경", "011031-1034567")
print(p1)
print('-' * 50)
p2 = PersonInfo("김연희", "020908-3279567")
print(p2)
print('-' * 50)
p3 = PersonInfo("박지윤", "030515-2944567")
print(p3)