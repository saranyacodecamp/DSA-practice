class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def delete_node(self,val):
        if not self.head:
            print("List is Empty")
            return
        if self.head.data == val:
            self.head = self.head.next
            return 
        curr = self.head
        while curr:
            if curr.data == val:
                prev.next = curr.next
                curr.next = None
                return
            prev = curr
            curr = curr.next
        print("Item Not in the List")

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data,"-->")
            curr = curr.next

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        
        print(self.print_list())





l1 = linkedlist()
l1.add_node(5)
l1.add_node(4)
l1.add_node(6)
l1.add_node(7)
l1.add_node(8)
l1.print_list()
l1.delete_node(4)
#l1.print_list()
l1.reverse_list()