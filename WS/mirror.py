def mirror(sentence):
   senli = list(sentence)
   senli.reverse()
   senstr = ''.join(senli)
   if senstr == sentence:
       return True
   else:
       return False

   # hstr_len = len(str)//2
   # last_index = len(sentence)-1
   #
   # for i in range(hstr_len):
   #     if sentence[i] != sentence[last_index-i]:
   #         return False
   #  return True

print(mirror("abcba"))
print(mirror("abcbda"))
print(mirror("zbbz"))