"""
Problem:
- we are given an array of nums
- and an integer val
- we need to remove the elements from the array with integer val
- then return the size of the array with all the elements no equal to the given val
- what comes after those elements doesn't matter
- these elements need to be front of the row

Ex:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

>> Although the return value needs to only be an integer, the method does expect us to change the nums
in place. Since it will take the first n elements of the nums array to check. n being whatever number
we will return

Approach:
- we can use list comprehension to remove all occurences of val in the list
- and return the length of the list

"""

def remove_element(nums, val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            del(nums[i])
    
    return len(nums)

# improved complexity
def remove_element(nums, val):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k