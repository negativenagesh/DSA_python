class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,front=None,rear=None,item_count=0):
        self.front=front
        self.rear=rear
        self.item_count=item_count

    def is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        q=Queue(data)
        if self.is_empty():
            self.front=q
        else:
            self.rear.next=q
            self.rear=q
        self.item_count+=1

    def deque(self):
        if self.is_empty():
            raise IndexError("Item does not exist")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=None
            self.front.next=self.front
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            print(self.front.item)

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item 

    def size(self):
        return self.item_count
    

q=Queue()
q.enqueue(100)
