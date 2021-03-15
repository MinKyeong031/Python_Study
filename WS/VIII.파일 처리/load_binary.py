import array

with open('data.bin', 'rb') as file:
    data = array.array("B")
    data.fromfile(file, 3)

# for item in data:
#     print(item)
print(data)