import random
import time
#main
mat = []
n = int(input("Enter size: "))
for i in range(n*n):
      a = []
      for j in range(n*n):
            val = random.randint(1,n*n)
            a.append(val)
            time.sleep(.1)
            print(val,end=" ")
      mat.append(a)
      print()
print("\nROWS: \n")
for i in range(n*n):
      temp = []
      time.sleep(.1)
      for j in range(n*n):
            temp.append(mat[i][j])
      print("ROW ",i+1,": ",temp)
print("\nCOLUMNS: \n")
for i in range(n*n):
      temp = []
      time.sleep(.1)
      for j in range(n*n):
            temp.append(mat[j][i])
      print("COLUMN ",i+1,": ",temp)
print("\nSUB MATRIX: \n")
for i in range(n):
      for j in range(n):
            print("SUB: ",i+j+1)
            for ii in range(n):
                  for jj in range(n):
                        time.sleep(.1)
                        print(mat[(n*i)+ii][(n*j)+jj],end=" ")
                  print()
            print()
      print()
