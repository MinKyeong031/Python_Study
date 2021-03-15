def day_to_weekday(day):
    week = ["금", "토", "일", "월", "화", "수", "목"]
    return week[day%7]+"요일"

for i in range(1, 32):
    print(day_to_weekday(i))