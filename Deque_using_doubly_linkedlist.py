class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev

class Deque:
    def __init__(self,front=None,rear=None,item_count=0):
        self.front=front
        self.rear=rear
        self.item_count=item_count

    def is_empty(self):
        if self.front==None:
            print("Empty Deque")
        else:
            print("Not empty Deque")

    def insert_front(self,item):
        i=Node(item,self.front)
        if self.front is not None:
            self.front=i
        else:
            self.front=i
