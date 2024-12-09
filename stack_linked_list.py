class node():
    def __init__(self,val,next) -> None:
        self.val = val
        self.next = next

class stack():
    def __init__(self) -> None:
        self.top = None
        self.count = 0
    
    def push(self,val):
        next_node = node(val,self.top)
        self.top = next_node;
        self.count+=1

    def pop(self):
        if not self.top:
            return None
        val = self.top.val
        self.top = self.top.next
        self.count-=1
        return val
    
    def peek(self):
        if not self.top:
            return None
        return self.top.val

    def print_stack(self):
        current = self.top
        while current:
            print(current.val)
            current = current.next

my_stack = stack()
for i in range(1,4):
    my_stack.push(i)
