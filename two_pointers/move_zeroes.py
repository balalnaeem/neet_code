"""
PROBLEM: Move Zeroes
- we are given an array of nums
- we need to move all 0's to the end of the array
- which other non zero integers, maintain the order in place
- we must do that in place without making a copy of the array

EXAMPLES:
In: [0, 1, 0, 3, 12]
out: [1, 3, 12, 0, 0]

in: [0]
out: [0]

in: [0. 1, 1, 0, 0, 2]
out: [1, 1, 2, 0, 0]

in: [1, 2, 3]
out: [1, 2, 3]

- nums won't be empty
- nums can include negative integers

We want to minimize the number of operation done.

BREAKDOWN:
- so we can iterate over the array and everytime, we come across a 0
  we delete it and append a 0 at the end.
  while append is 0(1)
  del would be 0(n) since rest of the elements will have their index changed
  so that won't be very efficient
Lets look at the array a bit more closely:

[0, 1, 0, 3, 12]
 ^  ^
 [1, 0, 0, 3, 12]
     ^  ^
[1, 0, 0, 3, 12]
    ^     ^
[1, 3, 0, 0, 12]
       ^  ^
 [1, 3, 0, 0, 12]
        ^     ^  
[1, 3, 12, 0, 0]
       ^      ^ 

APPROACH: 
- So we can have 2 pointers; one at 0 index and one at index 1
- left and right pointer
- left pointer should be at 0
  if left pointer is at a non zero value, we move it forward one step
- while the right pointer should be at non zero value
  if the pointer is at a zero value we move it forward one step
- and if the left is at 0 and right pointer is at non-zero, we switch their places
- after switching the places we go through the previous two steps again
- loop continues until right pointer is < len(arr)
- we are hoping to minimize the operations like this

ALGO:
DEF method
    left pointer 0
    right pointer 1

    while right pointer is less than arr length:
        if left pointer value == non zero:
            left pointer moves right on step.
        if right pointer value == zero or left pointer == right pointer:
            move right to find non zero.
        
        if left pointer == zero and right pointer == not zero:
            switch their places in the array


[0, 1, 1, 0, 0, 2]
 l  r
[1, 0, 1, 0, 0, 2]
    l  r
[1, 1, 0, 0, 0, 2]
       l        r
[1, 1, 2, 0, 0, 0]
"""
def move_zeroes(nums):
    left = 0
    right = 1

    while right < len(nums):
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != 0:
            left += 1
        if nums[right] == 0 or left == right:
            right += 1

# A more readable version
def move_zeroes(nums):
    left = 0  # Pointer for the next non-zero position

    for right in range(len(nums)):  
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)

print(nums)
             