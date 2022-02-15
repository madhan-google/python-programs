import sys

row = set()
col = set()
def clear():
      row.clear()
      col.clear()
      return

if __name__ == '__main__':
      r = sys.stdin
      t = int(input())
      for tt in range(t):
            mat = []
            n = int(input())
            for i in range(n):
                  mat.append(map(int,r.readline().split()))
            dia_sum , bad_row , bad_col = 0 , 0 , 0
            for i in range(n):
                  dia_sum += mat[i][i]
                  for j in range(n):
                        row.add(mat[i][j])
                        col.add(mat[j][i])
                  if row.size() is not n:
                        bad_row += 1
                  if col.size() is not n:
                        bad_col += 1
                  clear()
                  
            print("Case #{} : {} {} {}".format(tt,dia_sum,bad_row,bad_col))
