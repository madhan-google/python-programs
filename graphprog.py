import time
from collections import defaultdict
adj = defaultdict(list)

def addEdge(s,e):
	adj[s].append(e)

def printGraph(v):
	for i in range(v):
		print("Vertex ",i,": ")
		for j in range(len(adj[i])):
			print(adj[i].get(j),end="->")
		print("\n")

if __name__ == '__main__':
	v = int(input("ENter vertices size: "))
	while True:
		s = int(input())
		e = int(input())
		if s is -1 and e is -1:
			break
		else:
			addEdge(s,e)
	printGraph(v)
