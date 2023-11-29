class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data)
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print(node.data)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder_traversal(root)

print("Preorder Traversal:")
preorder_traversal(root)
           
print("Postorder Traversal:")
postorder_traversal(root)