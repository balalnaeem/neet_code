"""
PROBLEM
We are given an array of sorted integers. We need to find the index of a given integer.
EXAMPLES
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5 => 4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10 => 9
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1 => 0

BREAKDOWN
- We can use binary search to solve this problem.
- We can start by setting the left pointer to 0 and the right pointer to the length of the array - 1.
- We can then calculate the middle index by adding the left and right pointers and dividing by 2.
- We can then compare the middle element with the target element.
- If the middle element is equal to the target element, we can return the middle index.
- If the middle element is less than the target element, we can set the left pointer to the middle index + 1.
- If the middle element is greater than the target element, we can set the right pointer to the middle index - 1.
- We can continue this process until the left pointer is greater than the right pointer.
- If the left pointer is greater than the right pointer, we can return -1.
- This is because the target element is not in the array.

PSEUDOCODE
1. Set left pointer to 0.
2. Set right pointer to length of array - 1.
3. While left pointer is less than or equal to right pointer:
    4. Calculate middle index by adding left and right pointers and dividing by 2.
    5. If middle element is equal to target element, return middle index.
    6. If middle element is less than target element, set left pointer to middle index + 1.
    7. If middle element is greater than target element, set right pointer to middle index - 1.
8. Return -1.
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1