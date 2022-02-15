def maxDivide(a,b):
      while a%b == 0:
            a /= b
      return a;

def isUgly(n):
      n = maxDivide(n,2)
      n = maxDivide(n,3)
      n = maxDivide(n,5)
      if n == 1:
            return 1
      else:
            return 0

T = int(input())
for t in range(1,T+1):
      un = int(input())
      i = 1
      count = 1
      while un > count:
            i+=1
            if isUgly(un):
                  count+=1
      print("Case #{}: {}".format(t,i))      
