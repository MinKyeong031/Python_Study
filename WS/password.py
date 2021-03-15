def is_password(pw):
    ch1 = False
    ch2 = False
    ch3 = False
    ch4 = False
    ch5 = False

    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 5<=len(pw) and len(pw)<=7:
        ch1 = True

    if pw[-1] == "*" or pw[-1] == "#":
        ch2 = True

    if not pw in "`~!@#$%^&-_+=|\\<>;:'\" ":
        ch3 = True

    for i in pw:
        if i in "0123456789":
            num[int(i)] += 1

    for i in range(0, 10):
        if num[i] >= 3:
            ch4 = False
            break
        else:
            ch4 = True

    for i in pw[:-1]:
        if i in "*#":
            ch5 = False
            break
        else:
            ch5 = True

    if ch1 == True and ch2 == True and ch3 == True and ch4 == True and ch5 == True:
        return True
    else:
        return False

print(is_password('1234*'))   #True
print(is_password('987654#'))   #True
print(is_password('25558#'))   #False
print(is_password('234878#'))   #True
print(is_password('23#878#'))   #False
print(is_password('#598'))   #False