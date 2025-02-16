"""
PROBLEM:
- we are given an array of nums.
- we need to find x values that are greater than x in the nums array
- x number of values, and also greater than the number x
- if no such values exist, return -1

EXAMPLES:
Input: nums = [3,5]
Output: 2
There are 2 (x) values that are greater than or equal to 2 (x). So 2 is x. And we return 2

Input: [0, 4, 3, 0, 4]
Output: 3

There are 3 values that are >= 3. So x is 3. So we return 3.


Breakdown:
say an array's length is the maximum possible x.
if an array has 5 values, there might be 5 values greater than or equal to 5
but there is only one x if the array is special

when we start iterating over the array to find the x element
  - when we see the first value that is greater than 1
  - x is 1
  - now the next value has to be greater than or equal >=2 for us to consider making x 2
  - and if we come across that, x is 2
  - now the next value has to be greater than or equal to 3 for us to consider making x 3
  - this continues like this until we have iterated over the all the nums

"""

def special_array(nums):
    for i in range(len(nums) + 1):
        count = 0
        for num in nums:
            if num >= i:
                count += 1
        
        if count == i:
            return i
    
    return -1