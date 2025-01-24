"""
PROBLEM:
- Given an array of size n, return the majority element
- majority element == element that appears more than n/2 times
- majority element always exists

EXAMPLES:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

EDGE CASES
- empty array
- array of size 1

[1, 2, 3, 2, 2, 2, 2, 3]
sorting the array doesn't really help

"""
def majority_element(nums):
    res = {}
    for num in nums:
        if res.get(num):
          res[num] += 1
        else:
          res[num] = 1
    return next((key for key, value in res.items() if value == max(res.values())), None)

# print(majority_element([3,2,3]))

# A better approach
def majority_element_2(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
  
print(majority_element_2([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2]))