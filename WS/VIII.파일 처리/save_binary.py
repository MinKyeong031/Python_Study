byte_list = bytes([255, 0, 127])
with open('data.bin', 'wb') as file:
    file.write(byte_list)

data = hex(127)
print(data)
print(bin(7))