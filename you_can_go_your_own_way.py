#main
T=int(input())
for t in range(1,T+1):
    n=int(input())
    s=str(input())
    ans = ""
    for i in range(len(s)):
        if s[i] == "S":
            ans += "E"
        else:
            ans += "S"
    print("Case #",t,": ",ans)
