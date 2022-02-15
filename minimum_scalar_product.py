#main
v1 = []
v2 = []
t = int(input())
for t in range(1,t+1):
    ans = 0
    n = int(input())
    for i in range(n):
        v1.append(int(input()))
    for i in range(n):
        v2.append(int(input()))
    v1.sort()
    v2.sort(reverse=True)
    for i in range(n):
        ans += v1[i] * v2[i]
    print("Case #",t,": ",ans)

        
