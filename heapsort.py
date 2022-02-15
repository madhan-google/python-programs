import random

def sort(arr,n):
	for i in range(0,int(n/2-1)):
		heapify(arr,n,i)
	j = n-1
	while j >= 0:
		t = arr[0]
		arr[0] = arr[j]
		arr[j] = t
		heapify(arr,j,0)
		j -= 1

def heapify(arr,n,i):
	large = i
	l = i * 2 + 1
	r = i * 2 + 2
	if l < n and arr[l] > arr[large] :
		large = l
	if r < n and arr[r] > arr[large] :
		large = r
	if large != i:
		t = arr[i]
		arr[i] = arr[large]
		arr[large] = t
		heapify(arr,n,large)

if __name__ == "__main__":
	n = int(input("Enter size: "))
	arr = []
	for i in range(n):
		arr.append(random.randint(1,n*2))
		print(arr[i],end=" ")
	sort(arr,n)
	print("\n")
	print(arr)