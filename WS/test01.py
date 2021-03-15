def exclude_first_name(name):
    names=name.split(",")
    result=[]
    for i in names:
        result.append(i[1:])
    return result

first_names = exclude_first_name("황광희,이효리,김지훈,이지은,고수")
print(first_names)

def is_pangram(sentence):
    right = "abcdefghijklmnopqrstuvwxyz"
    s = sentence.replace(" ","").lower()
    for i in right:
        if i not in s:
            return False
    return True

# 알파벳이 모두 포함된 문자열은 True 값을 반환
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Jock nymphs waqf drug vex blitz"))
# 알파벳 중 글자가 하나씩 빠진 문자열은 False 값을 반환
print(is_pangram("The quik brown fox jumps over the lazy dog"))
print(is_pangram("The quick brown fx jumps over the lazy do"))
print(is_pangram("ock nymphs waqf drug vex blitz"))
print(is_pangram("Jock nymphs waqf drug vex bltz"))


def num_to_list(num):
    list=[]
    zeroCnt = len(str(num))-1
    for i in (str(num)):
        list.append(int(i)*(10**zeroCnt))
        zeroCnt-=1
    return list

li1 = num_to_list(54321)
li2 = num_to_list(1004)
print(li1)
print(li2)
# 리스트의 모든 값을 더하는 sum 함수를 반환된 리스트에 적용하면 원래 값을 반환해야 함
print(sum(num_to_list(54321)))
print(sum(num_to_list(1004)))

def print_weekday(day):
    num = day%7
    day_tuple={0:"화요일",1:"수요일",2:"목요일",3:"금요일",4:"토요일",5:"일요일",6:"월요일"}
    print(day_tuple[num])

for i in range(1,32):
    print_weekday(i)


def snakecase_to_camelcase(sentence):
    s = sentence.split("_")
    camelcase=""
    for i in range(1, len(s)):
        camelcase+=s[i][0].upper()+s[i][1:]
    camelcase=s[0]+camelcase
    return camelcase

cc1 = snakecase_to_camelcase("hello")
cc2 = snakecase_to_camelcase("hello_world")
cc3 = snakecase_to_camelcase("snake_case_to_camel_case")
print(cc1)
print(cc2)
print(cc3)