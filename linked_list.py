class node():
    def __init__(self,val,next_node):
        self.val = val
        self.next_node = next_node

class linked_list():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def create_head(self,val):
        if not self.head:
            self.head = node(val,None)
            self.size+=1
            return 1
        return 0
    
    def push_back(self,val):
        if self.create_head(val):
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = node(val,None)
        self.size+=1

    def push_front(self,val):
        if self.create_head(val):
            return
        self.head = node(val,self.head)
        self.size+=1
    
    def pop_back(self):
        if not self.head:
            return None
        current = self.head
        before = None
        while current.next_node:
            before = current
            current = current.next_node
        if not before:
            self.head = None
        else:
            before.next_node = None
        self.size-=1
        return current.val        

    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next_node
    
    def insert(self,val,index):
        if index>=self.size:
            self.push_back(val)
            return
        if index<0:
            return
        current_index = 0
        current = self.head
        before = None
        while current_index<index:
            before = current
            current = current.next_node
            current_index+=1
        if not before:
            self.push_front(val)
            return
        before.next_node = node(val,current)
        self.size+=1

    def pop(self,index):
        if index<0 or index>=self.size:
            return
        before = None
        current = self.head
        current_index = 0
        while current_index<index:
            before = current
            current =current.next_node
            current_index+=1
        if not before:
            current = self.head
            self.head = None
        else:
            before.next_node = current.next_node
        self.size-=1
        return current.val

    def for_each(self,callback):
        current = self.head
        while current:
            callback(current.val)
            current = current.next_node
    
    def __len__(self):
        return self.size

arr = [1,2,3,4,5]
linked_list1 = linked_list()
for i in arr:
    linked_list1.push_back(i)
linked_list1.for_each(lambda i:print(i+1,end=" "))