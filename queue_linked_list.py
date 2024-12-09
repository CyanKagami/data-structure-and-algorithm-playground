class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.before = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    
    def enqueue(self,val):
        if not self.front:
            self.front = node(val)
            self.rear = self.front
        else:
            self.rear.next = node(val)
            temp = self.rear
            self.rear = self.rear.next
            self.rear.before = temp
        self.count+=1
    
    def dequeue(self):
        if not self.front:
            return None
        if self.count == 1:
            val = self.front.val
            self.front = None
            self.rear = None
            self.count-=1
            return val
        val = self.rear.val
        self.rear = self.rear.before
        self.rear.next = None
        self.count-=1
        return val
    
    def queueFront(self):
        if not self.front:
            return None
        return self.front.val
    
    def queueRear(self):
        if not self.rear:
            return None
        return self.rear.val

q1 = queue()
for i in range(1,5):
    q1.enqueue(i)
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.queueFront(),q1.queueRear(),q1.count)