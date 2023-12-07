class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def insert(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            temp =self.right.find_min()
            self.data = temp
            self.right = self.right.delete(temp)
        return self
    
    def search(self,data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
            
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


# perform basic operation insert, delete, search , find min,find max
 
root = Node(1)
root.insert(100)
root.insert(24)
root.insert(46)

inorder(root)

root.delete(24)

print("-----------")
inorder(root)

print(root.search(100))
