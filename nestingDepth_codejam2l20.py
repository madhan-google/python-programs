T = int(input())
for t in range(1,T+1):
      s = str(input())
      ans = ""
      brc = 0
      for i in range(len(s)):
            val = int(s[i])
            while val > brc:
                  brc+=1
                  ans+="("
            while val < brc:
                  brc-=1
                  ans+=")"
            ans+=str(val)
      while brc > 0:
            ans+=")"
            brc-=1
            
      print("Case #{}: {}".format(t,ans))
      
