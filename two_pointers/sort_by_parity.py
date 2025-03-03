"""
PROBLEM:
- we are given an integer array
- move all the even integers in the beginning
- and odd integers to the end
- any array that satisfies this is acceptable

EXAMPLES:
in: [3,1,2,4]
out: [2,4,3,1] or [4, 2, 3, 1] or [4, 2, 1, 3]

in: [0]
out: [0]

BREAKDOWN:
- a brute force solution would be very simple.
  - iterate over the array separating the evens and odds into two different arrays
  - append the odds to the evens and return
  - but it's not really ideal
- what we want to do is use a two pointer approach here
- a pointer on the left and a pointer on the right

if the left is odd
  - if the right is even, switch their places, move each pointer one step
  - if the right is odd as well, move the right inward one step, left stays where it is 
if the left is even
  - left pointer moves one step forward
  - if the right is odd, move the right to the left one step
  - if the right is even, right pointer stay where it is

[3, 1, 2, 4]
 l        r 
...........
 [4, 1, 2, 3]
     l  r
...........
[4, 2, 1, 3]

"""

def sort_by_parity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
      if nums[left] % 2 != 0:
          if nums[right] % 2 == 0:
              nums[left], nums[right] = nums[right], nums[left]
              left += 1
          right -= 1
      else:
          if nums[right] % 2 != 0:
              right -= 1
          left += 1
    
    return nums

print(sort_by_parity([0]))


    
        
            