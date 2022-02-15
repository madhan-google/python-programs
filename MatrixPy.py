import random
n=int(input())
A=[]
B=[]
for i in range(n):
      arr=[]
      ar=[]
      for j in range(n):
            arr.append(random.randint(1,n))
            ar.append(random.randint(1,n))
      A.append(arr)
      B.append(ar)
print("Matrix A\n")
for i in range(n):
      for j in range(n):
            print(A[i][j],end=" ")
      print()
print("\nMatrix B\n")
for i in range(n):
      for j in range(n):
            print(B[i][j],end=" ")
      print()
print("\nMatrix Addition\n")
for i in range(n):
      for j in range(n):
            print(A[i][j]+B[i][j],end=" ")
      print()
print("\nMatrix Subtraction\n")
for i in range(n):
      for j in range(n):
            print(A[i][j]-B[i][j],end=" ")
      print()
print("\nMatrix Multiplication\n")
for i in range(n):
      for j in range(n):
            print(A[i][j]*B[i][j],end=" ")
      print()
print("\nMatrix Division\n")
for i in range(n):
      for j in range(n):
            print(A[i][j]/B[i][j],end=" ")
      print()
