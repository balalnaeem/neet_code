"""
PROBLEM:
- we are given an array of integers
- we need to choose two pairs out of that. Four different indices
- And return the difference between the product of pair 1 and pair 2
- The pairs we choose, should have the maximum possible product difference in the array
- Basically one pair should result in the largest product
  and one pair should result in the smallest product

array length will always be 4 or more
and each integer will be positive

EDGE CASES:
empty array --> No!
Zeroes --> No!

EXAMPLES:
Input: nums = [5,6,2,7,4]
Output: 34

Input: nums = [4,2,5,9,7,4,8]
Output: 64

2 largest numbers product - 2 smallest numbers product

APPROACH:
- seems like if we just sort this array, the problem fizzles
- we can get the first two and last two integers and solve the issue

"""

def max_prod_diff(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[-1] * sorted_nums[-2] - sorted_nums[0] * sorted_nums[1] 

# print(max_prod_diff([5,6,2,7,4]))
# print(max_prod_diff([4,2,5,9,7,4,8]))

# A better approach
def max_prod_diff(nums):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max2, max1 = max1, num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num
    
    return max1 * max2 - min1 * min2


print(max_prod_diff([5,6,2,7,4]))
print(max_prod_diff([4,2,5,9,7,4,8]))