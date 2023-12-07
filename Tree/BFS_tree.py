from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def level_order(self,root):
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node.data)
                q.append(node.left)
                q.append(node.right)
        return res



    
# perform Level order Traversal ---->

root = Node(1)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -", root.level_order(root))
