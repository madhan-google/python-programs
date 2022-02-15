import random
import time
class node:
      def __init__(self,data):
            self.next = None
            self.data = data

def insert(head,data):
      newnode = node(data)
      if head == None:
            head = newnode
      else:
            tail = head
            while tail.next != None:
                  tail = tail.next
            tail.next = newnode
      return head
def printList(head):
      if head != None:
            curr = head
            while curr != None:
                  time.sleep(.2)
                  print(curr.data,end="->")
                  curr = curr.next
                  

if __name__ == "__main__":
      n = int(input("Enter size:"))
      head = None
      for i in range(n):
            head = insert(head,random.randint(1,n*5))
      printList(head)
