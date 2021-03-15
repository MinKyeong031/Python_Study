# file = open('file.txt', 'r')
# data = file.read()
# file.close()
# print(data)

file = open('phonebook.txt', 'r', encoding='utf8')
data = []
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace('\n', '')
    data.append(line)
file.close()

# file = open('phonebook.txt', 'r', encoding='utf8')
# data = file.readlines()
# file.close()

for record in data:
    record = record.split(',')
    print('이름 : ' + record[0])
    print('전화번호 : ' + record[1].replace('\n', ''))