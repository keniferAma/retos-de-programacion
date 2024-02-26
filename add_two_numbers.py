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
It is guaranteed that the list represents a number that does not have leading zeros."""


def selecter(list_: list) -> list:
    previous_list = []
    final_number = ''
    for i in list_:
        if len(str(i)) >= 2:
            for n in str(i):
                previous_list.append(int(n))
        else:
            previous_list.append(i)

    for j in range(len(previous_list) - 1, -1, -1):
        final_number += str(previous_list[j])

    return int(final_number)




def add_two_numbers(list_1: list, list_2: list) -> list:
    org_list_1 = selecter(list_1)
    org_list_2 = selecter(list_2)

    return org_list_1 + org_list_2


lista1 = [1423, 56, 3, 78]
lista2 = [14, 56, 3, 74, 21]

print(add_two_numbers(lista1, lista2))









