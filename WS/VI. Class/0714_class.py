#클래스 연습
class Classroom:
    def __init__(self, student, teacher):
        self.student = student
        self.teacher = teacher

    def __str__(self):
        return f'이 교실의 학생은 {self.student}, 선생님은 {self.teacher}입니다.'
    
    def get_student(self):
        return self.student
    
    def get_teacher(self):
        return self.teacher

교실2_1 = Classroom(['강종아', '권혜수', '최지안'], '호식쌤')
print(교실2_1)

교실2_2 = Classroom(['형연이', '연지이', '지우우'], '유병석쌤')
print(교실2_2)

print(f'2-1반 교실의 담임선생님은 {교실2_1.get_teacher()}')
print(f'2-2반 교실의 학생은 {교실2_2.get_student()}')

학년2솦과 = [교실2_1, 교실2_2]
for 교실 in 학년2솦과:
    print(교실)