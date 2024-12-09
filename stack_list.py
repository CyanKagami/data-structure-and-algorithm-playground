class stack():
    def __init__(self) -> None:
        self.val = []
        self.count = 0
    
    def push(self,val):
        self.val.append(val)
        self.count+=1

    def pop(self):
        if not self.val:
            return None
        self.count-=1
        return self.val.pop()
    
    def peek(self):
        if not self.val:
            return None
        return self.val[-1]

    def print_stack(self):
        for i in reversed(self.val):
            print(i)

my_stack = stack()
for i in range(1,4):
    my_stack.push(i)
my_stack.print_stack()
