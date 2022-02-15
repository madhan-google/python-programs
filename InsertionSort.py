import random
import time

arr = []
n = int(input("ENter size: "))
tot = 0
for i in range(n):
      arr.append(random.randint(1,n*5))
      tot += arr[i]
print("Elements are: ",arr)
for i in range(1,n):
      j = i-1
      key = arr[i]
      while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
      arr[j+1] = key
print("Sum of Array: ",tot)
print("Sorted Elements Are: ",arr)
for i in range(n):
      tot += arr[i]
print("Sum of Array: ",tot)
