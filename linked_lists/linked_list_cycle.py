"""
PROBLEM:
Given head of a linked list, determine if the linked list has a cycle
A linked list has a cycle, if by continuously pointing to the next node, you reach
some node again.

EDGE CASES:
- An empty linked list? head is none

EXAMPLE:
[3, 2, 0, -4]
-4 points to 2 as it's next node
TRUE

APPROACH:

- we can start iterating over the linked with two pointers
- on each iteration the fast pointer will traverse two nodes
- while slow pointer will traverse 1 node
- if there is a cycle in the list, the list, two pointers at some point will point to the same node
- if the fast pointer reaches None, return false
- we have to be careful though
- if the fast pointer is at the last node, the next pointer would be none, we need to take the condition in consieration

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False