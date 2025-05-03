"""
PROBLEM:
- we are given a sorted(asc) array of distinct integers
- we are given a target value
- we need to return the index of target value in the array
- if the target value does not exist in the array, we should return the supposed index it should have
  existed at in the array

EXAMPLES:
[1, 3, 5, 6], 5
2

[1, 3, 5, 6], 2
1

[1, 3, 5, 6], 7
4

Must write an algorithm that is O(log n) runtime complexity.

BREAKDOWN:
- we can iterate over the array
- and at any time we come across an int equal to our target we return that index
- if we come across an integer that is greater than our target, we return that index

"""

# def search_insert(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target or nums[i] > target:
#             return i
    
#     return len(nums)

def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
      
    

print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))