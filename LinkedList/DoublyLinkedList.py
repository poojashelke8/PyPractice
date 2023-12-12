class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
class DLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            raise Exception("Empty List!")
        
    def insert_at_start(self,data):
        if self.head is None:
            self.insert_at_empty(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_empty(data)
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def traversing(self):
        if self.head is None:
            print("No elements")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n = n.next

new_linkedList = DLinkedList()
new_linkedList.insert_at_empty(10)
new_linkedList.insert_at_start(20)
new_linkedList.insert_at_end(30)
new_linkedList.traversing()
   