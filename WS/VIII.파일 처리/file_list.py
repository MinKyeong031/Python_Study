#p.229
import os
data = os.listdir('.')
#print(data)
for d in data:
    print(d)
    print("is directory? : " + str(os.path.isdir(d))) #file
    print("is file? : " + str(os.path.isfile(d))) #file