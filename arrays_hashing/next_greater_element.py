"""
PROBLEM:
- we are given two integer arrays
- num1 and num2
- num1 is a sub array of num2
- for each integer in num1, we need to find the greater element in num2
- all integers in num1 and num2 are unique
- if there is no greater element, we use -1

What is a greater element?
- first higher val integer to the right

EXAMPLES:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]

EDGE CASES:
empty num1?

Simple brute force solution?

- initialize an empty res array
- iterate over the num1 array
- find the index of each element in num2 array
- iterate over num2 starting from that index until you find a greater element
- if you do find one, append to res array
- if you don't find one, append -1 to the res array
- return the res array

"""

def next_greater_element(nums1, nums2):
    res = []
    for num in nums1:
        start_idx = nums2.index(num)
        greater_element = -1
        for idx in range(start_idx + 1, len(nums2)):
            if nums2[idx] > num:
                greater_element = nums2[idx]
                break
        res.append(greater_element)
    return res

# There has to be a better way
def next_greater_element_2(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = num
        stack.append(num)
    
    while stack:
        next_greater[stack.pop()] = -1
    
    return [next_greater[num] for num in nums1]

print(next_greater_element_2([4, 1, 2], [1,3,4, 2, 6]))
# print(next_greater_element_2([2,4], [1,2,3,4]))