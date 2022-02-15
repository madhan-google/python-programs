def checkItHaveNine(value):
    a = []
    while value > 0:
        a.append(value%10)
        value /= 10
    for i in range(len(a)):
        if i == 9:
            return False
    return True

#main
T = int(input())
for t in range(1,T+1):
    con = 0
    a = int(input())
    b = int(input())
    for i in range(a,b+1):
        if checkItHaveNine(i) and i%9 != 0:
            con +=1
    print("Case #",t,": ",con);
