def isTidy(num):
      s = str(num)
      for i in range(len(s)-1):
            if int(s[i]) > int(s[i+1]):
                  return False
      return True


#main
T = int(input())
for t in range(1,T+1):
      n = int(input())
      j = n-1
      while j >= 0:
            if isTidy(j):
                  print("Case #",t,": ",j)
                  break
            j -=1
