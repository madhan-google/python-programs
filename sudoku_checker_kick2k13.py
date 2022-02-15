import random
if __name__ == '__main__':

      arr = []
      T = int(input())
      for t in range(1,T+1):
            n = int(input())
            ans = "Yes"
            for i in range(n*n):
                  a = []
                  for j in range(n*n):
                        val =  random.randint(1,n*n)
                        a.append(val)
                        #print(val,end=" ")
                  arr.append(a)
                  print()
            #row
            for i in range(n*n):
                  d = {}
                  for j in range(n*n):
                        temp = arr[i][j]
                        if temp != 0 and temp in d:
                              ans = "No"
                              break
                        d[val] = 1
                  if ans is "No":
                        break
            #column
            for i in range(n*n):
                  d = {}
                  for j in range(n*n):
                        temp = arr[j][i]
                        if temp != 0 and temp in d:
                              ans = "No"
                              break
                        d[val] = 1
                  if ans is "No":
                        break
            #sub matrix
            for i in range(n):
                  for j in range(n):
                        for ii in range(n):
                              d = {}
                              for jj in range(n):
                                    temp = arr[(n*i)+ii][(n*j)+jj]
                                    if temp != 0 and temp in d:
                                          ans = "No"
                                          break
                                    d[val] = 1
                              if ans is "No":
                                    break
            print("\nCase #",t,": ",ans)
      
      
