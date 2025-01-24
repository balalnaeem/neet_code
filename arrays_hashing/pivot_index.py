"""
PROBLEM:
- given an array of nums, return the pivot index.
What is pivot index?
- it's index where sum of all the numbers strictly to the left
  is equal to sum of all the numbers to the right.
- Return the left most pivot index
- if no such index exists, return -1
- left most pivot index? surely there is only one pivot index

EDGE CASES?
- if the sum of all the elements to the right of first index is 0
- then first index(e.g. 0) is the pivot index

EXAMPLES:
Input: nums = [1,7,3,6,5,6]
Output: 3

Input: nums = [1,2,3]
Output: -1

Input: nums = [2,1,-1]
Output: 0

input: nums = [-1, 1, 2]
Output: 2

APPROACH:
- we can have two pointers iterating over the array
- once both pointer are at the equal sum and there is only one index between them
- that index is pivot index
- if no such point comes, we let the pointers continue all the way
- and if one index before last one, they reach zero
  then the left edge or the right edge is the pivot

PSEUDOCODE:
left total = 0
right total = 0
left_pointer = 0
right_pointer = -1

a while loop
while left pointer < len(arr) -1 and right pointer > -(len(arr))
on each iteration
  - left total += arr[left pointer]
  - right total += arr[right pointer]
  - if left total == right total and left pointer + right pointer == 1
      return left pointer + 1
  - left pointer += 1
  - right pointer -= 1
if right total == 0
  return 0
if left total == 0
  return 0
return -1

[2, 1, -1]
"""

# Failed attempt
def pivot_index_fail(nums):
    left_total = 0
    right_total = 0
    left_idx = 0
    right_idx = -1

    while left_idx < len(nums) - 1 and right_idx > -(len(nums)):
        left_total += nums[left_idx]
        if left_total == right_total:
            return left_idx + 1
        right_total += nums[right_idx]
        if right_total == left_total:
            return right_idx - 1
        left_idx += 1
        right_idx -= 1
    if right_total == 0:
        return 0
    if left_total == 0:
        return len(nums) - 1
    return -1



# A better approach
def pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total - nums[i] - left_sum
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1

print(pivot_index([2, 1, -1]))
print(pivot_index([-1, 1, 2]))
print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))