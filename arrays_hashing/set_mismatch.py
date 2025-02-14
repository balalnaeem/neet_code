"""
PROBLEM:
- we have a list of integers s
- list originally had all numbers from 1 to n
- due to an error, one of the numbers got duplicated.
- resulting in loss of a number and repetition of a number
- nums we are given, is after the error
- find the number that occurs twice and the one that's missing and return them in an array

EXAMPLES:
[1, 2, 2, 4]
[2, 3]

[1, 1]
[1, 2]

[1, 3, 3, 4]
[3, 2]

[1, 2, 2, 3, 4]
[2, 5]

[1, 3, 4, 5, 5]


Approach:
Trying to come up with an approach that will not involve multiple iteration over the nums array
- we can set two varibales to None
  1. repeated_num
  2. missing_num
- we can start iterating over array
  but first sort it in place
- Now before the iteration starts, we need to have an expected number
- expected number will start from 1, as the nums are supposed to be from 1 to n
Now inside the iteration, logic can be as follows:
  - if the current num is greater than expected num
    we know expected nums is missing.
    we set the missing_num = expected_num
    we increment the expected_num for the next iteration
  - if the current num is != to expected_num, and is equal to previous num
    - we know the current num is the repeated_num, so we can update that
    - don't have to update the expected num, coz the next num could be expected_num,
  - if next is greater then it would fall into the first part of the conditional

 [1, 2, 2, 4] 
PSEUDO CODE:
DEFINE METHOD find_error_nums(nums):
SET repeated_num to NONE
SET missing_num to NONE
SET expected_num to 1

SORT the nums in place

START LOOP iterate over the nums
IF current_num IS NOT EQUAL TO expected_num:
  TWO POSSIBILITIES HERE:
  1. expected_num is missing
    IF current_num > expected_num
      it's missing_num,
      SET missing_num to expected_um
      INCREMENT expected_num to += 1 for the next iteration
  2. current_num is being repeated
    ELSE
      SET the repeated_num to current_num
      DON't increment because repetition so we need to expect the same number again
ELSE current num is EQual to expected_num
  just increment the expected_num

return the [repeated_num, missing_num]

"""

# def find_error_nums(nums):
#     repeated_num = None
#     missing_num = None
#     expected_num = 1
#     nums.sort()

#     for cur_num in nums:
#         if cur_num != expected_num:
#             if cur_num > expected_num:
#                 missing_num = expected_num
#                 expected_num += 1
#             else:
#                 repeated_num = cur_num
#                 continue
#         expected_num += 1
#     return [repeated_num, missing_num]

# print(find_error_nums([1, 3, 4, 5, 5]))
# print(find_error_nums( [1, 2, 2, 4] ))
# print(find_error_nums( [1, 1] ))

from collections import Counter

def find_error_nums(nums):
    res = [0, 0]
    counts = Counter(nums)

    for num in range(1, len(nums) + 1):
        if counts[num] == 2:
            res[0] = num
        if counts[num] == 0:
            res[1] = num
    
    return res