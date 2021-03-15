# #p.234
# file = open('file.txt', 'w') #write
# file.write('hello')
# file.write('\n')
# file.write('world')
# file.close()

try:
    file = open('file.txt', 'w', encoding='utf-8')
    file.write('hello')
    file.write('월드')
finally:
    file.close()

with open('phonebook.txt', 'w', encoding='utf-8') as file:
    file.write('일미림,010-11111-111\n')
    file.write('이미림,010-2222-222\n')

