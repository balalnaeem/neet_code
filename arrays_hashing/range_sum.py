"""
PROBLEM:
- Given an integer array of nums, handle multiple queries of sum range
- implement the NumArray class
- initialize the object with integer array nums
- in the function sum_range(left, right)
  return the sum of elements of nums, including left and right

EXAMPLES:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

[1, 2, 3]
[0, 1, 3]

"""

class NumArray:
    def __init__(self, nums):
        self.nums = nums
    
    def sum_range(self, left, right):
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum


# A better approach
class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
    
    def sum_range(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]