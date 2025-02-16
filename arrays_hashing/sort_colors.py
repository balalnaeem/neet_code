"""
- we are given an array of nums
- nums consists of 0's 1's and 2's
0 = red
1 = white
2 = blue

we want to sort the array in place so that same colors are adjacent to each other
and order is red white and blue
so 001122

main thing is to sort the array in place

Examples:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Breakdown:
- we are sorting an array in place
- we need to iterate over the array and update it in real time
- we can have two pointers: left and right
- while right pointer traverses the array, left stays where it is
- if right pointer finds a value that is less than the left pointer
  values exchange places
- this continues till the left pointer reaches the last element in the array
"""

def sort_colors(nums):
    for left in range(len(nums)):
        right = left + 1

        while right < len(nums):
            if nums[left] > nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
            right += 1
    return nums