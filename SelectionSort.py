import random
import time

arr = []
n = int(input("Enter sizze: "))
print("Elements are: ")
for i in range(n):
      val = random.randint(1,n*10)
      arr.append(val)
      print(val,end=" ")
print("\nSorted Elements Are: ")
for i in range(n):
      min_indx = i
      for j in range(i+1,n):
            if arr[min_indx] > arr[j]:
                  time.sleep(.1)
                  min_indx = j
      arr[i],arr[min_indx] = arr[min_indx],arr[i]
      print(arr[i],end=" ")
