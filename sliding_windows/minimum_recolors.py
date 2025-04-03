"""
PROBLEM:
- we are given a string of letters W and B
- W means white
- B means black
- we are also given an integer K
- k is the desired number of consecutive black letters
- in one operation we can recolor a W to B
- we need to return the minimum number of operations needed to get k consecutive black letters

- k will always be <= to n

EXAMPLES:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3

Input: blocks = "WBWBBBW", k = 2
Output: 0

BREAKDOWN:
- we need to get k length substrings from the string
HOW do we get substring? [start:end]
- we start from 0 index and on each substring, we check the number of W in that substring, which means, number of operations needed
- if in any substring number of operations, are lower than the previous number of operations, we set the new value

APPROACH:
- set min operations to positive infinity
- start a loop
  > on each iteration get a substring starting from 0 index ending at k index
  > count the number of W's in that substring
  > if they are less than the min_ops var, set that as new value
  > increment start and end by 1 each
- condition of while loop be till end <= len of the string
- return the min_ops
"""

def min_recolors(blocks, k):
    min_ops = float('inf')
    start = 0
    end = k
    while end <= len(blocks):
        temp = blocks[start:end]
        ops_needed = temp.count('W')
        if ops_needed < min_ops:
            min_ops = ops_needed
        start += 1
        end += 1
    
    return min_ops

print(min_recolors("WBWBBBW", 2))

# Big O of 1
def min_recolors(blocks, k):
    ops_needed = blocks[:k].count('W')
    min_ops = ops_needed

    for i in range(k, len(blocks)):
        if blocks[i - k] == 'W':
            ops_needed -= 1
        
        if blocks[i] == 'W':
            ops_needed += 1
        
        min_ops = min(min_ops, ops_needed)

    return min(min_ops, ops_needed)