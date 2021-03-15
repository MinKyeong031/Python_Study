from datetime import datetime

today = datetime.now()
print(f'현재 날짜와 시각 : {today}')
print(today.year, today.month, today.day, today.hour, today.minute, today.second)

day = datetime(2020, 12, 25, 0, 0, 0)
print(day)
print(day-today)

first_day = datetime(2020, 5, 5, 0, 0, 0)
print(today-first_day)

birthday = datetime(2003, 4, 13, 0, 0, 0)
print(today-birthday)