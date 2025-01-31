"""
PROBLEM:- 
- given an array of integers, return number of good pairs in the array.
- what is a good pair?
  a good pair is where two elements (a and b) are equal to each other,
  and a's index is lower than b's.
  Basically a comes in before b in the array

EXAMPLES:- 
Input: nums = [1,2,3,1,1,3]
Output: 4

Input: nums = [1,1,1,1]
Output: 6

Input: nums = [1,2,3]
Output: 0

EDGE CASES:-
empty array?
just one element in the array
negative numbers?

Can't think of many edge cases situations that could affect the algo

APPROACH:
- we need some sort of iteration logic
- we can have two pointers
- one that would be current index
- and second that would be the checking index
- current index would always be behind the checking index
- current index val would be checked against each checking index val
- based on comparison, we will increase the number of good pairs counter
"""

def good_pairs(nums):
    good_pairs = 0
    n = len(nums)
    current_idx = 0

    while current_idx < n:
        checking_idx = current_idx + 1
        while checking_idx < n:
            if nums[current_idx] == nums[checking_idx]:
                good_pairs += 1
            checking_idx += 1
        current_idx += 1
    
    return good_pairs

print(good_pairs([1,2,3,1,1,3]))
