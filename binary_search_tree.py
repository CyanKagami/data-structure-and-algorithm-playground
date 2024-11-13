class node():
    def __init__(self,val,left,right) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.quantity = 1

class tree():
    def __init__(self) -> None:
        self.root = None
    
    def add_root(self,val):
        if not self.root:
            self.root = node(val,None,None)
            return 1
        return 0

    def add_leaf(self,val):
        if self.add_root(val):
            return
        current = self.root
        before = None
        direction = ""
        while current:
            if val==current.val:
                current.quantity+=1
                return
            if val<current.val:
                before = current
                direction = "left"
                current = current.left
            else:
                before = current
                direction = "right"
                current = current.right
        if direction == "left":
            before.left = node(val,None,None)
        else:
            before.right = node(val,None,None)
    
    def print_tree(self):
        if not self.root:
            return
        self.recursive(self.root)
    
    def recursive(self,leaf:node):
        if leaf.left:
            self.recursive(leaf.left)
        for _ in range(leaf.quantity):
            print(leaf.val)
        if leaf.right:
            self.recursive(leaf.right)

    def find(self,val):
        current = self.root
        while current:
            if current.val == val:
                return True
            if val<current.val:
                current = current.left
            else:
                current = current.right
        return False
    
    def remove(self,val,quantity):
        current = self.root
        before = None
        direction = ""
        while current:
            if current.val == val:
                if current.quantity>=quantity:
                    pass
arr = [1,1,3,7,5,9,4,2]
tree1 = tree()
for i in arr:
    tree1.add_leaf(i)
print(tree1.find(1))