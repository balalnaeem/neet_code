"""
PROBLEM:
- we are given two integer arrays, nums1 and nums2
- return an array of intersection
- intersection = elements that exist in both the arrays
- result array must be unique and the order doesn't matter

EXAMPLE:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

- all positive numbers in both arrays
- no empty arrays
- if no intersection, we return the empty array
[1, 1] <=> [2, 2]
[]

Approach:
- we can use two hashmaps to store the numbers of two arrays
- then lookup in the two hashmaps whether the number was in both arrays
- or we can count one array, and iterate over the other array while checking through that hashmap

"""
from collections import Counter

def intersection(nums1, nums2):
    res = set()
    counts1 = Counter(nums1)
    
    for num in nums2:
        if counts1[num] > 0:
            res.add(num)
    
    return list(res)

print(intersection([1,2,2,1], [2,2]))