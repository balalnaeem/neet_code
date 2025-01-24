"""
PROBLEM: Invert Binary Tree
Given the root of a binary tree, invert the tree and return it's root.

What does inversion mean?
As every node in Binary tree has two nodes, a left and a right. Inversion would mean swithcing their places.
Left becomes right, and right becomes left.

Example:
  4
1   7

becomes
  4
7   1

Example 2:
      1
  2       5
3   4   6   7

becomes
      1
  5       2
4   3   7   6


EDGE CASES:
- emtpy tree

Approach:
- We are given a root node.
- first we will check if it has left or right node.
- if it does, we will switch their places in the tree
- and then we can check whether the left or right node has any child nodes
- if they do we can move down to their level and switch their places
- maybe a recursive method can work here

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
      
        if root.left or root.right:
            temp = root.right
            root.right = root.left
            root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = TreeNode(1)
root.left = TreeNode(2)

sol = Solution()
print(sol.invertTree(root))