def validate_password(password):
    count = 0
    num_flag = False
    len_flag = False

    if 4 <= len(password) <= 10:
        len_flag = True

    for pw in password:
        if not "A" <= pw <= "Z" and "a" <= pw <= "z":
            count += 1
        if not pw in "`~!@#$%^&*-_+=|\\<>;:'\" " and pw in ",.?/()":
            count += 1
        if pw in "1234567890":
            count += 1
            num_flag = True

    if num_flag == True and count == len(password) and len_flag == True:
        return True

    return False

print(validate_password("1a."))
print(validate_password("PassWORD"))
print(validate_password("bu..letea"))
print(validate_password("bubb!et2a"))
print(validate_password("b()bb12 tea"))
print(validate_password("b()bb12tea"))
print(validate_password("p?55w0rd"))
