"""
PROBLEM:
- we have a flowerbed in which plots are represented by 1's and 0's
- flowers cannot be planted in adjacent plot
- 1's mean the plot is planted
- 0's mean the plot is empty
- given an integer n
- return True if it is possible to plant n plants, False otherwise

EXAMPLES:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

EDGE CASES:
can there be one plant in the flowerbed? Yes
if we are given [0] and n = 1
we return True

if we are given [0, 0] and n = 1
we return True

if we are given [0, 0, 0] and n = 2
we return True because [1, 0, 1] is possible

so if the second element is 0 the first can be a flower
and second last element is a 0 the last can be a flower
0ne zero alone can be a flower


APPROACH:
- We will need to iterate over the array of 1's and 0's
- and we will need to check on each iteration for few things
  - if prev index is -1 and next index's value is 0, we can plant the flower
  - if prev index is 0 and next index is 0, we can plant the flower
  - if prev index is 0 and next index is == to the len of the list, we can plant the flower
- We will have to be changing the arr in place as we iterate so we can correctly decide the 
  number of possible flowers
- every time we plant a flower, we count the number of flowers,
  no need to count again to avoid the iterating again

"""

def can_place_flowers(arr, n):
    counter = 0
    for idx in range(len(arr)):
        if len(arr) == 1 and arr[idx] == 0:
            arr[idx] == 1
            counter += 1
            continue
        if idx == 0 and arr[idx] == 0 and arr[idx + 1] == 0:
            arr[idx] = 1
            counter += 1
        if idx == len(arr) - 1 and arr[idx] == 0 and arr[idx - 1] == 0:
            arr[idx] = 1
            counter += 1
        if arr[idx] == 0 and arr[idx - 1] == 0 and arr[idx + 1] == 0:
            arr[idx] = 1
            counter += 1
    return counter >= n

# print(can_place_flowers([0,0,1,0,0], 1))

# A better approach

def can_place_flowers_2(flowerbed, n):
    f = [0] + flowerbed + [0]

    for i in range(1, len(f) - 1): # skip the first index and the last index
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            f[i] = 1
            n -= 1

    
    return n <= 0

print(can_place_flowers_2([0,0,1,0,0], 3))