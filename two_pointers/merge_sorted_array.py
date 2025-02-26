"""
PROBLEM:
- we are given two integer arrays, nums1 and nums2
- we are also given two integers m and n
- m the size of other than 0 integers in nums1
- n the size of integers in nums2
- both arrays are sorted in ascending order
- we have to merge both the arrays in ascending order as well
- but nums1 should be the final merged array, not another new array
- nums1 has 0's added to it at the end, 0's equal the length of nums2
- we don't return anything
- just modify the nums1 in place

EXAMPLES:
input: [1, 2, 3, 0, 0, 0] [2, 5, 6] n = 3
output: [1, 2, 2, 3, 5, 6]

input: [1], [] n = 0
output: [1]

input: [0], [1], n = 1
output: [1]

Breakdown:
- so we have two arrays and two numbers
- both arrays are sorted
- both numbers tell us how many elements are in the arrays
- first array, though, has 0's at the end equal to the size of second array
- elements are sorted in ascending order, but zero's are still at the end
- do we even need the zeros?

we need to merge both the arrays, and the merged array should also be in a ascending
- of course it's very easy to achieve it with O(n log(n))
  - append the array 2 into nums1 in place of zeroes
  - and sort it in place
- but we want to do efficiently
- we can use a temp array
- while going over the both the arrays, insert into the temp array
- then go over the temp array, and insert accordingly into nums1

[1 2 3 0 0 0]    [2 5 6]
 ^                ^


"""

def merge(nums1, m, nums2, n):
    temp = []
    idx1 = 0
    idx2 = 0

    while idx1 < m and idx2 < n:
        if nums1[idx1] <= nums2[idx2]:
            temp.append(nums1[idx1])
            idx1 += 1
        else:
            temp.append(nums2[idx2])
            idx2 += 1
    
    while idx1 < m:
        temp.append(nums1[idx1])
        idx1 += 1
    
    while idx2 < n:
        temp.append(nums2[idx2])
        idx2 += 1
    
    for i in range(len(temp)):
        nums1[i] = temp[i]
