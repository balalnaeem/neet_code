"""
PROBLEM:
- we are given two integers arrays nums1 and nums2
- return an array of size 2
    - where first element is an array of all distinct integers of nums1 that are not present in nums2
    - and second element is an array of all distinct integers of nums2 that are not present in nums1
- integers maybe returned in any order

EXAMPLES:
nums1 = [1, 2, 3], nums2 = [2, 4, 6]
output: [[1, 3], [4, 6]]

nums1 = [1, 2, 3, 3], nums2 = [1, 1, 2, 2]
output: [[3], []]

nums1 = [1], nums2 = [2]
output: [[1], [2]]

BREAKDOWN:
- so the brute force solution could look something like this:
  - we iterate over the first array, on each iteration we check the whether the current
  element is included in the second array, if not we save it into an array.
  - we repeat the same process vice versa for second array and save the result into an array.
- add these two arrays into the answer array which we can return
- as we can see it is not very efficient.
- so we need to find a solution, that is not this inefficient

- we can turn the lists into sets and then check for inclusion?

"""
def find_difference(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    answer = [[], []]

    for num in set_nums1:
        if num not in set_nums2:
            answer[0].append(num)
    
    for num in set_nums2:
        if num not in set_nums1:
            answer[1].append(num)
    
    return answer

print(find_difference([1, 2, 3], [2, 4, 6]))