"""
PROBLEM:
- we are given an array of nums of n integers
- integers range in the array are between 1 and n(length)
- find all the missing integers from 1 and n

EXAMPLES:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]

EDGE CASES:-
No missing integer ==> empty array

"""
def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    store = set(range(1, n + 1))
    
    for num in nums:
        store.discard(num)
    
    return list(store)

