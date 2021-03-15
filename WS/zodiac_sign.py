# def zodiac_sign(birth):
#     zodiac = ["원숭이", "닭", "개", "돼지", "쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양"]
#
#     year = int(birth.split("-")[0])
#     sign = zodiac[year%12]
#
#     return f'{year}년도는 {sign}의 해 입니다.'

def zodiac_sign(birthday):
    year = birthday.split("-")[0]
    띠 = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
    return f'{띠[(int(year)+8)%12]}띠'

print(f'다니엘 래드클리프는 {zodiac_sign("1989-7-23")}')
print(zodiac_sign("1990-10-21"))
print(zodiac_sign("1999-10-21"))
print(zodiac_sign("2003-10-21"))
