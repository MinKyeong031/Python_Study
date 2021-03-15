'''
#print(func_a(teacher_name))

#teacher_name함수에 파라미터로 선생님 이름을 넣으면,
#리턴은 그선생님의 과목을 리턴한다

#print(func_a('우호식'))		#'수학'

'''
def func_a(name):
    major = {'우호식' : '수학', '임정훈' : '파이썬', '백현정' : '자바',
             '이호걸' : '씨쁠쁠', '이재민' : '자료구조', '정혜선' : '영어',
             '박향규' : '체육', '권지웅' : '과학', '이아람' : '음악',
             '박성래' : '수학', '최영진' : '국어', '이대형' : '국어',
             '유병석' : '파이썬', '박지우' : 'jsp, 프로그래밍', '신혜정' : 'php'}
    #return major.get(name)
    return major[name]

print(func_a('우호식'))
print(func_a('유병석'))
print(func_a('신혜정'))
print(func_a('임정훈'))
print(func_a('이형섭'))