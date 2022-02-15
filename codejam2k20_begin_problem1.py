def check(t):
      for i in range(len(t)):
            for j in range(i+1,len(t)):
                  if t[i] == t[j]:
                        return True
      return False

T = int(input())
for t in range(1,T+1):
      mat = []
      n = int(input())
      r = []
      c = []
      dia = 0
      row = 0
      col = 0
      for i in range(n):
            a = []
            for j in range(n):
                  a.append(int(input()))
            mat.append(a)
      
      for i in range(n):
            dia += mat[i][i]
            for j in range(n):
                  r.append(mat[i][j])
                  c.append(mat[j][i])
            if check(r):
                  row += 1
            if check(c):
                  col += 1
      print("Case #",t,": ",dia," ",row," ",col)
