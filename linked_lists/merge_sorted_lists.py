"""
PROBLEM:
- We are given the heads of two sorted linked lists list1 and list2
- merge the two lists in one sorted linked list
- return the head of the new list
- new list should be made up of nodes from list1 and list2

EXAMPLE:
- input
list1 = [1, 2, 4]
list2 = [1, 3, 5]

- output
[1, 1, 2, 3, 4, 5]

- output linked list is also a sorted linked list
- length of the two lists can vary
- if both lists are empty, we return an empty linked list

AL:
- We need to create a new list with an empty receiving node
- And then compare the value of list1 and list2
- on each comparison, add the smaller value to the new list's receiving node
- after each comparison move the receiving node forward to the end
- after we are done with the lists we need to check the edge cases
- in case one list is empty in which case we return the other list

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def mergeTwoLists(self, list1, list2):
        new_node = ListNode()
        temp = new_node
        while list1 and list2:
          if list1.val < list2.val:
              temp.next = list1
              list1 = list1.next
          else:
              temp.next = list2
              list2 = list2.next
          temp = temp.next # move the receiving node
        
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        
        return new_node.next
            

              

  

# [1, 2, 4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
# [1, 3, 5]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(5)

solution = Solution()

result = solution.mergeTwoLists(list1, list2) # [1, 1, 2, 3, 4, 5]

print(result)
