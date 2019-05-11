"""
LeetCode #2: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
Approach: 
 - Think as if how I would perform arithmetic by hand
 - output is the sum of current pointer to list1, list2 and carry (if any)

Pseudocode:
carry = 0
while (both lists not empty):
    if one of the list is exhausted then just set the value to 0, else set data from list 1 and 2
    compute sum = list1 value + list2 value + carry value
    if sum > 10, update carry and return sum
    #Update result list
    create a new node (temp) with value of sum
    check if result list is initalised -> set self.head = temp   
    move the pointer until the next pointer for both lists are None

Tricks:
  - An inner class is an instance of a class created within the body of another class
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        newNode = Node(data)
        newNode.next = self.head # self.head is the pointer to the prev new node
        self.head = newNode
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        while (l1 is not None or l2 is not None):
            data1 = l1.data if l1 else 0
            data2 = l2.data if l2 else 0
            sum = data1 + data2 + carry
            carry = sum // 10
            sum = sum % 10
            print("Sum is {} and Carry is {}".format(sum, carry))
            #Create new node with sum as data
            temp = Node(sum)
            #If this is the first node set as head of the resultant list, else continue to add on to the list
            if self.head == None:
                self.head = temp
            else:
                prev.next = temp
            # Set the resultant node for next insertion
            prev = temp
            # Move first and second pointer to next node
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    

llist1 = LinkedList()
llist1.addNode(6)
llist1.addNode(4)
llist1.addNode(9)
llist1.addNode(5)
llist1.addNode(7)
print("The first list is: ", end="")
llist1.PrintList()
llist2 = LinkedList()
llist2.addNode(4)
llist2.addNode(8)
print("\nThe second list is: ", end="")
llist2.PrintList()
print("\n")
# add the two linked list and see the result
result = LinkedList()
result.addTwoNumbers(llist1.head, llist2.head)
print("\nThe resultant list is: ", end="")
result.PrintList()
print("\n")
