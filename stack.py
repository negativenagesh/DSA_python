class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        if len(self.items)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    
    def push(self,item):
        self.items.append(item)

    def pop(self,item):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if len(self.items)==0:
            print("Stack is empty")
        else:
            return self.items[-1]

    def define_size(self):
        return f"Size of stack is: {len(self.items)}"
    
    def print_stack(self):
        if not self.is_empty():
            for i in self.items:
                print(self.items[i])  
