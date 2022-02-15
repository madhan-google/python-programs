import random
import time

class node:
      def __init__(self,data):
            self.data = data
            self.right = None
            self.left = None
def insert(root,data):
      if root is None:
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
def preorder(root):
      if root is not None:
            time.sleep(.1)
            print(root.data,end=" ")
            preorder(root.left)
            preorder(root.right)
def inorder(root):
      if root is not None:
            time.sleep(.1)
            inorder(root.left)
            print(root.data,end=" ")
            inorder(root.right)
def postorder(root):
      if root is not None:
            time.sleep(.1)
            postorder(root.left)
            postorder(root.right)
            print(root.data,end=" ")
def levelorder(root):
      if root is None:
            return
      else:
            h = height(root)
            print("\nTree Height: ",h)
            print("\nLevel Order Traversal: ")
            for i in range(1,h+1):
                  printlevel(root,i)
def height(root):
      if root is None:
            return 0
      else:
            l = height(root.left)
            r = height(root.right)
            if l > r:
                  return l+1
            else:
                  return r+1
def printlevel(root,level):
      if root is None:
            return 
      if level is 1:
            time.sleep(.1)
            print(root.data,end=" ")
      elif level > 1:
            printlevel(root.left,level-1)
            printlevel(root.right,level-1)

#main
n = int(input("enter size: "))
root = None
print("Elements are: ")
for i in range(n):
      val = random.randint(1,n*10)
      root = insert(root,val)
      print(val,end=" ")
levelorder(root)
print("\nPre Order Traversal: ")
preorder(root)
print("\nIn Order Traversal: ")
inorder(root)
print("\nPost Order Traversal: ")
postorder(root)
