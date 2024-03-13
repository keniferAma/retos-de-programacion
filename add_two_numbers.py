"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
TO KEEP IN MIND: A linked list is based on separate nodes with a single data, this node has the hability to 
access the next node, and in order to that, can acces the next data. so in linked lists, we can't access the data through 
their indexes."""


def selecter(list_: list) -> list:
    result = ''
    for i in list_[::-1]:
        if len(str(i)) >= 2:
            for j in str(i)[::-1]:
                result += j
        else:
            result += str(i)

    return int(result)


def add_two_numbers(list_1: list, list_2: list) -> list:
    org_list_1 = selecter(list_1)
    org_list_2 = selecter(list_2)

    return org_list_1 + org_list_2


lista1 = [1423, 56, 3, 78]
lista2 = [14, 56, 3, 74, 21]
lista3 = [21, 5, 0, 6, 0, 0]
lista4 = [0, 0 , 0]
lista5 = [0, 0, 0]

print(add_two_numbers(lista4, lista5))



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def adding_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    current = head
    carry = 0

    while l1 or l2 or carry:
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10) #The divmod() function is a built-in function in Python that takes two numbers as
        #arguments and returns a tuple containing the quotient and the remainder of the division operation12. 
        
        current.next = ListNode(out)
        current = current.next
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return head.next



# Python linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Create a linked list
linked_list = LinkedList()
linked_list.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Link first node to second and second node to third
linked_list.head.next = second
second.next = third
third.next = fourth

# To access the second node's data, we have to traverse from the head
print(linked_list.head.next.data)  # Output: 20
print(linked_list.head.next.next.data)
print(linked_list.head.next.next.next.data)



# @return a ListNode
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next




# prove with a regular insert, delete, search in a linked list #
    

def find(head, data):
        """Function to find a value inside the linked list"""
        current = head
        result = False
        while current != None:
            value = current.data
            if data == value:
                result = True
                break
            
            current = current.next

        return result

    
class PrincipalNode:
    """This class will gives the single nodes values"""
    def __init__(self, data=None, next=None): # This None because if we're at the end of the node, this must be none.
        self.data = data
        self.next = next


class PrincipalLink:
    """This class will give the head of the list"""
    def __init__(self):
        self.head = PrincipalNode()


    def add(self, data):
        new_node = PrincipalNode(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node


    def get_length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        
        return total
    

    def print_length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        
        print(total)


    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
            

        print(elements)

    
    def search(self, index):
        current_node = self.head
        list_length = self.length()
        counter = -1
        while index < list_length:
            if index == counter:
                print(current_node.data)
                break

            current_node = current_node.next
            counter += 1
        else:
            print({'Value not found': 'Index out of range.'})

    def delete(self, index):
        current_node = self.head
        list_length = self.get_length()
        counter = 0

        while index < list_length:
            if index == counter:
                current_node.next = current_node.next.next
                break
            elif index == list_length:
                current_node.next = None

            current_node = current_node.next
            counter += 1

        else:
            print({'Value not found': 'Index out of range.'}) 


    
   

nodes = PrincipalLink()
nodes.add(1)
nodes.add(3)
nodes.add(4)
nodes.display()
nodes.delete(1)
nodes.display()
nodes.add(121)
nodes.add(78)
nodes.add(192)
nodes.add(8)
nodes.display()
nodes.delete(6)
nodes.display()