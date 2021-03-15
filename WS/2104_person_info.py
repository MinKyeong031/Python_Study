class PersonInfo:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.gender = [None, '남자', '여자', '남자', '여자'][int(id_number[7])]
        if '00' <= self.id_number[8:10] <= '08':
            self.region = '서울'
        elif '09' <=  self.id_number[8:10] <= '12':
            self.region = '부산'
        elif '13' <=  self.id_number[8:10] <= '15':
            self.region = '인천'
        elif '16' <=  self.id_number[8:10] <= '25':
            self.region = '경기'
        elif '26' <=  self.id_number[8:10] <= '34':
            self.region = '강원'
        elif '93' <=  self.id_number[8:10] <= '95':
            self.region = '제주'

    def __str__(self):
        return f'{self.name}님의 주민등록번호는 {self.id_number}입니다.\n'\
               + f'{self.name}님의 YY/MM/DD은 {self.id_number[:2]}/{self.id_number[2:4]}/{self.id_number[4:6]}입니다.\n'\
               + f'{self.name}님은 {self.gender}입니다.\n'\
               + f'{self.name}님의 출생 지역은 {self.region}입니다.'


p1 = PersonInfo("김민경", "011031-1034567")
print(p1)
print('-' * 50)
p2 = PersonInfo("김연희", "020908-3279567")
print(p2)
print('-' * 50)
p3 = PersonInfo("박지윤", "030515-2944567")
print(p3)