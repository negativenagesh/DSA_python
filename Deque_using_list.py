class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        if len(self.items)==0:
            print("Empty Deque")
        else:
            print("Deque is not empty")
    
    def insert_first(self,item):
        self.items.insert(0,item)
    
    def insert_rear(self,item):
        self.items.insert(-1,item)
    
    def delete_front(self):
        if self.items==None:
            raise IndexError("Empty Deque")
        else:
            self.items.pop(0)
    
    def delete_rear(self):
        if not self.items==None:
           self.items.pop()
        else:
            raise IndexError("Empty Deque")
        
    def get_front(self):
        if not self.items==None:
            return self.items[0]
        else:
            raise IndexError("Empty Deque")
    
    def get_rear(self):
        if not self.items==None:
            return self.items[-1]
        else:
            raise IndexError("Empty Deque")

    def size(self):
        return len(self.items)
    
d=Deque()
