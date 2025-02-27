"""
PROBLEM: Remove Duplicates
- we are given an array of ints sorted
- we want to remove the duplicates such that each unique element appears once
- The relative order should be kept the same
- return the number of unique elements
- so the number of unique elements is k
- so modified nums will have all the unique elements as first k
- remaining elements and the size is not important
- only the first k elements

EXAMPLES:
in: [1,1,2]
out: 2
modified nums = [1, 2, _]
elements after the k length don't matter


input: [0,0,1,1,1,2,2,3,3,4]
Output: 5
modified nums = [0,1,2,3,4,_,_,_,_,_]

Breakdown:
- we can call uniq on the array
- iterate over the uniq array and insert each element into nums
- return length of the uniq array
but this is not efficient. And since it uses another array, it is not in place change

- we will have to change two pointer approach
- left pointer and right pointer
- left pointer will keep track of the repeating values
- while the right pointer keeps track of next value in line

we get length of nums
we set l and r pointers to 0
start a loop till right pointer is < n
value at left pointer = value at right pointer
start another loop until you reach the next val
now r points to the next value
we break out of this loop
and move the l to the next value
r is either this value or next value after repetitions
we repace them anyway
then again find the next value
return l in the end because that would be the number of elements replaced on total
"""
def remove_duplicates(nums):
    unique_nums = list(dict.fromkeys(nums))
    idx = 0
    for num in unique_nums:
        nums[idx] = num
        idx += 1
    
    return len(unique_nums)

# two pointer approach
def remove_duplicates(nums):
    n = len(nums)
    l = r = 0

    while r < n:
        nums[l] = nums[r]
        while r < n and nums[l] == nums[r]:
            r += 1
        
        l += 1
    
    return l

