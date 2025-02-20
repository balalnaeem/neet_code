"""
Problem:
- we are given an array of nums
- where nums[i] represent the score of that student
- we are also given an integer k
- pick the scores of k students from the array
  - so that the diff between highest and lowest of the k scores is minimized
- Return min possible difference

Examples:
in: [90], k= 1
out: 0

There is only one element, and only on possibility of the element to be picked which is 90
so 90 - 90 = 0

in: [9, 4, 1, 7] k = 2
out: 2

So here we have to pick two scores:
We can pick:
9, 4
9, 1
9, 7
4, 1
4, 7
7, 1

The min difference is if we pick 9 and 7. Which is 2
So almost had to get all possible combinations or 2 elements
if it was 3 elements, we would have to get all possible combinations of 3 elements

BREAKDOWN:
- since we need to get the scores of k students from the array
- and then we need to return the minimum possible diff from the possible score combinations
- Looks like what we need to do is get all possible combinations
- so we need to divide the array into sub array of k sizes
- how do we create sub arrays of k sizes
- we iterate over the array with index access
- on each iteration we slice the array from the next index, getting one less element, because one would be
the current element
- there would be a loop inside a loop
- the inside loop will start from one index next step
- and slice the array from there till one less the required sub array size because one would be the current index
"""

def minimum_diff(nums, k):
    nums.sort()
    l, r = 0, k - 1
    res = float("inf")
    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        l += 1
        r += 1
    return res

print(minimum_diff([9, 4, 1, 7], 3))