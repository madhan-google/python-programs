import time
#main
s = "abcdefghijklmnopqrstuvwxyz"
ss = str(input("Enter string: "))
for i in range(len(ss)):
      count = 1
      for j in range(len(s)):
            if s[j] == ss[i]:
                  count += 1
      print(ss[i],": ",count)
