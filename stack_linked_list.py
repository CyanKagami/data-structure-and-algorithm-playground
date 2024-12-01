class node():
    def __init__(self,val,next) -> None:
        self.val = val
        self.next = next

class stack():
    def __init__(self) -> None:
        self.head = None
    
    def push(self,val):
        next_node = node(val,self.head)
        self.head = next_node;

    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val
    
    def peek(self):
        if not self.head:
            return None
        return self.head.val

    def print_stack(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

my_stack = stack()
for i in range(1,4):
    my_stack.push(i)
