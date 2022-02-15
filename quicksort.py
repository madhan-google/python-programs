
def partition(arr,start,end):
      pInd = start
      pivot = arr[end]
      for i in range(start,end):
            if arr[i] <= pivot:
                  t = arr[i]
                  arr[i] = arr[pInd]
                  arr[pInd] = t
                  pInd += 1
      temp = arr[pInd]
      arr[pInd] = arr[end]
      arr[end] = temp
      return pInd

def sort(arr,start,end):
      if start < end:
            pInd = partition(arr,start,end)
            sort(arr,start,pInd-1)
            sort(arr,pInd+1,end)

if __name__ == "__main__":
      n = int(input("ENter size:"))
      arr = []
      for i in range(n):
            arr.append(int(input()))
      sort(arr,0,n-1)
      print(arr)
