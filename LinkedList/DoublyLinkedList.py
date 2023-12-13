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

    def insert_after_ele(self, x, data):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_ele(self,ele,data):
        if self.head is None:
            print("list is empty")
            return
        else:
            current = self.head
            while current is not None:
                if current.data == ele:
                    break
                current = current.next
            if current is None:
                print("item not in list")
            else:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev is not None:
                    current.prev.next = new_node
                current.prev = new_node


# ----------------------------------------------------------
# Deletion

    def delete_start(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is  None:
            self.head =  None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print('The list is Empty')
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def reverse_list(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev




        


new_linkedList = DLinkedList()
# new_linkedList.insert_at_empty(10)
new_linkedList.insert_at_start(20)
new_linkedList.insert_at_end(30)
# new_linkedList.traversing()
new_linkedList.insert_after_ele(20,50)
# new_linkedList.traversing()
new_linkedList.insert_before_ele(50,100)
# new_linkedList.traversing()
new_linkedList.delete_start()
# new_linkedList.traversing()
new_linkedList.delete_at_end()
new_linkedList.traversing()
new_linkedList.reverse_list()
print("After Reverse")
new_linkedList.traversing()

   