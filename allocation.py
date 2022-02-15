#main

T = int(input())
for t in range(1,T+1):
    arr = []
    n = int(input())
    dollar = int(input())
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    ans=0
    for i in range(n):
        if dollar >= arr[i]:
            dollar -= arr[i]
            ans += 1
    print("Case #",t,": ",ans)
    
