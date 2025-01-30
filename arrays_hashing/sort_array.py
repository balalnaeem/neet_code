"""
PROBLEM:
- given an array of integers
- sort the array in ascending order
- solve the problem without using any built in methods

EXAMPLES:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

EDGE CASES:
- negative numbers?
- empty array?
- array will only have one number
- we don't have floats since it is an array of integers

Brute Force Approach:
- we can have two pointers left and right
- left can be at 0 and right can at 1
- we compare left and right,
- if left is greater than right, we switch their places
  - and both pointers move forward one step
- if left is not greater than right, we don't switch places and move the pointers forward
- we just don't need to do go the last element again and need to iterate over one less element each time

"""

def sort_array(nums):
    n = len(nums)
    for j in range(n - 1, -1, -1):
        left_pointer = 0
        right_pointer = 1
        while right_pointer <= j:
            if nums[right_pointer] < nums[left_pointer]:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer += 1
    return nums


# This works but it does not pass the time limit on leetcode
# need to improve it
# so this is essentially a bubble sort, I will try and write a merge sort

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(arr_1, arr_2):
    combined = []
    i = 0
    j = 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            combined.append(arr_1[i])
            i += 1
        else:
            combined.append(arr_2[j])
            j += 1
    
    while i < len(arr_1):
        combined.append(arr_1[i])
        i += 1
    
    while j < len(arr_2):
        combined.append(arr_2[j])
        j += 1
    
    return combined
    
print(merge_sort([4, 2, 3, 1]))