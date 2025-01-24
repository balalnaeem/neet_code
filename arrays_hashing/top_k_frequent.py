"""
PROBLEM:
- we are given an array of integers
  - and another integer as input say k
- we have to find the most k frequented integers in the array
- so if the k is 2
- we have to find the 2 most frequented integers

EXAMPLE:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

AL:
- we need to iterate over the array of integers
- on each iteration we save the number as key in the iteration and 1 as it's value
- if the number already exists as key we can just increase the value by +1
- at the end of the iteration we have a dictionary with numbers and their frequency

Now to return the most frequencted k numbers
We can get the list of all the values, and get the max k values
and from those values traceback the keys.
"""

def top_k_frequent(nums, int):
  counts = {}
  for num in nums:
    if counts.get(num):
      counts[num] += 1
    else:
      counts[num] = 1
  return sorted(counts, key=counts.get, reverse=True)[:int]

nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))

# How to improve it




