
def merge(arr,left,right):
      nr = int(len(right))
      nl = int(len(left))
      i = j = k = 0
      while j < nl and k < nr :
            if left[j] <= right[k]:
                  arr[i] = left[j]
                  j += 1
            else:
                  arr[i] = right[k]
                  k += 1
            i += 1

def sort(arr):
      n = len(arr)
      if n < 2:
            return
      m = int(n / 2)
      left = []
      right = []
      for i in range(m):
            left.append(arr[i])
      for i in range(m,n):
            right.append(arr[i])
      sort(left)
      sort(right)
      merge(arr,left,right)

if __name__ == "__main__":
      arr = []
      n = int(input("Enter size: "))
      for i in range(n):
            arr.append(int(input()))
      sort(arr)
      print(arr)
