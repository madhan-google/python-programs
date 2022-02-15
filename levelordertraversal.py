import random
import time
class node:
      def __init__(self,data):
            self.data = data
            self.right = None
            self.left = None
def insert(root,data):
      if root == None:
            return node(data)
      else:
            curr = root
            if curr.data > data:
                  curr = insert(root.left,data)
                  root.left = curr
            else:
                  curr = insert(root.right,data)
                  root.right = curr
      return root
def printLevelOrder(root):
      if root == None:
            return
      else:
            h = height(root)
            print("\nTree Height is: ",h)
            print("\nLevel Order Traversal : \n")
            for i in range(1,h+1):
                  printLevel(root,i)
def height(root):
      if root is None:
            return 0
      else:
            l = height(root.left)
            r = height(root.right)
            if l < r:
                  return r+1
            else:
                  return l+1
def printLevel(root,level):
      if root is None:
            return 
      if level is 1:
            # time.sleep(.1)
            print(root.data,end=" ")
      elif level > 1:
            printLevel(root.left,level-1)
            printLevel(root.right,level-1)

#main
n = int(input("enter size: "))
root = None
print("elements are: ")
for i in range(n):
      val = random.randint(1,n*10)
      root = insert(root,val)
      print(val,end=" ")

printLevelOrder(root)
