#main
T = int(input())
arr = []
a = []
b = []
for t in range(1,T+1):
    n = int(input())
    for i in range(n):
        arr.append(int(input()))
        if arr[i]%2 == 0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    a.sort(reverse=True)
    b.sort()
    j = 0
    k = 0
    for i in range(n):
        if arr[i]%2 == 0:
            arr[i] = a[j]
            j += 1
        else:
            arr[i] = b[k]
            k += 1
    print("Case #",t,": ",arr)
    
    
