"""
PROBLEM:
- Given the root of a binary tree, return it's maximum depth.
- What is maximum depth of a binary tree?
  maximum depth is the number of nodes between root and the leaf alongside the longest path in the tree.

EDGE CASES:
- The tree could be empty

APPROACH:
- if the root is None
- if there is only one node in the tree
- if the tree had two children left or right
 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
      if not root:
          return 0
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))