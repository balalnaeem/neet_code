"""
PROBLEM:
- we are given an integer array nums
- and an integer k
- return True if
    1. there are two indices at which values are equal
    2. abs(i - j) <= k
- so in order to return true we need to satisfy these two conditions

EXAMPLES:
in: nums = [1, 2, 3, 1], k = 3
out: True
abs(0 - 3) is <= 3

in: nums = [1, 0, 1, 1], k = 1
out: True
abs(2 - 3) is <= 1

in: nums = [1, 2, 3, 1, 2, 3], k = 2
out: False
abs(0 - 3) is not <= 2
abs(1 - 4) is not <= 2
abs(2 - 5) is not <= 2

Data structures:
- array
- hash

BREAKDOWN:
- we have an array of integers
- first thing we have to do is detect if there is a duplicate
- and if we come across a duplicate we check the second condition, and return True if possible
- once we have gone over the array, we return False in the end

AL:
- we will have two pointers left and right
- left pointer will stay and right pointer moves one step at a time until the end of the array
   - if we find a duplicate, we check their indices, i - j absoulte and check if that is less than equal to k
   - if yes return True
   - if false, carry on
- right pointer when reaches end of the array
  - left pointer moves one step forward
  - right pointer is set to the one after the left
- left pointer reaches the end of the array, loop breaks

PSEUDO CODE:
- DEF contains_duplicate(nums, k):
    SET left to 0

    while left < length of nums - 1:
        SET right to left + 1
        while right < length of nums:
            if left value == right value and abs(left - right) <= k:
                return True
            right plus 1
        left += 1
    
    return False

"""

def contains_duplicates_old(nums, k):
    left = 0
    right = left + 1

    while left < len(nums) - 1:
        if nums[left] == nums[right] and abs(left - right) <= k:
            return True
        right += 1

        if right == len(nums):
            left += 1
            right = left + 1
    
    return False

# This is brute force and inefficient
# we can use hashmap so we would only have to iterate once and not loop within a loop

def contains_duplicates(nums, k):
    indices = {}

    for i in range(len(nums)):
        if nums[i] in indices and abs(indices[nums[i]] - i) <= k:
            return True
            
        indices[nums[i]] = i
    
    return False

# but we can do even better with the use of sliding window
# since abs(i -j) has to be less then equal to k
# we know that duplicates that are further distance than k itself will not be the answer
# because the indices' difference would be bigger than the k

def contains_duplicates_new(nums, k):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])

        if len(seen) > k:
            seen.remove(nums[i - k])
    
    return False

print(contains_duplicates_new([1, 2, 3, 4, 5, 1, 6, 1], 3))