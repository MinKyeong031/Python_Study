import sys
def repeater_str(msg, n):
    return msg * n

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(repeater_str(sys.argv[1], int(sys.argv[2])))
    else:
        print('사용법 : python repeater_str.py 문자열 숫자')
