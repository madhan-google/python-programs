import random
import time

def search(a,key):
    for i in range(len(a)):
        #print(a[i],"->",i+1,end="\n")
        if a[i] is key:
            return i
    return -1

#main
n = int(input("Enter size: "))
arr = []
print("Elements: ")
for i in range(n):
    val = random.randint(1,n*n)
    time.sleep(.08)
    arr.append(val)
    print(val,end=" ")
key = int(input("\nEnter search elements: "))
ss="Searching....."
for i in range(len(ss)):
    time.sleep(.2)
    print(ss[i],end="")
s = search(arr,key)
if s != -1:
    print("\nElement found in ",s+1," position")
else:
    print("\nElement not found")
