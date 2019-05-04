"""
Implementation of linked list data structure
@Author: Jason Ng

A linked list consists of a HEAD pointer that points to the first node
Each node contains a data field and a pointer to the next node
"""

class LinkedList():
    def __init__(self):
        self.head = None
    
    def printlist(self):
    # Linked list traversal - Print all values of the linked list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    # Lets create a linked list with 3 nodes
    
    # Start with empty list
    llist = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    llist.head = n1
    n1.next = n2
    n2.next = n3

    # Print list
    llist.printlist()