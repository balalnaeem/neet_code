"""
PROBLEM:
- we are given an integer array
- product is the product of all values
return 1 if product is positive
return -1 if product is negative
return 0 if product is zero

EXAMPLES:
[-1, -2, -3, -4, 3, 2, 1]
1

[1, 5, 0, 2, -3]
0

[-1, 1, -1, 1, -1]
-1

BREAKDOWN:
- at face seems like a simple enough problem.
- we can come up with a 0(n) solution
- iterate over the array and keep track of sign of the result of product
- return 1, -1, or 0 based on the final sign

Is there a more efficient way?
just to keep it simpler, we can just multiply 1 in place of actual integer
as we don't care about the integer values

AL:
- iterate over the array
- on each iteration, multiply 1 with either -1 or +1
- if current int is 0, return 0
- return 1 or -1 at the end
"""

def array_sign(nums):
    sign = 1
    for num in nums:
        if num > 0:
            sign *= 1
        elif num < 0:
            sign *= -1
        else:
            return 0
    
    return sign

print(array_sign([-1,1,-1,1,-1]))