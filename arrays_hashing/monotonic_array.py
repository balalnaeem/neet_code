"""
PROBLEM:-
- An array is monotonic if it is either monotone increasing or monotone decreasing
- for monotone increasing
  - for each next element will be either equal or greater than the previous element
- for monotone decreasing
  - for each next element will be either equal or less than the previous element

EXAMPLES:-
Input: nums = [1,2,2,3]
Output: true

Input: nums = [6,5,4,4]
Output: true

Input: nums = [1,3,2]
Output: false

APPROACH:
- we will have two loops but only one of them will run
- based on whether the array is increasing monotonic or decreasing monotonic
- we will decide which loop to run
- we can have two booleans that will help us decide which loop to run
"""

def is_monotonic(nums):
    increasing = nums[0] <= nums[-1]
    decreasing = nums[0] >= nums[-1]

    if increasing:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
    
    if decreasing:
        for j in range(len(nums) - 1):
            if nums[j] < nums[j + 1]:
                return False
    
    return True

print(is_monotonic([1,3,2]))