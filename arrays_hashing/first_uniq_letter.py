"""
PROBLEM:
- Given a string, find the first non-repeating character in it and return it's index
- if no non-repeating character exists, return -1

EXAMPLES:
leetcode
0

loveleetcode
2

aabb
-1

APPROACH:
- count the occurence of each letter in a string
- then iterate over the string
- first letter that you come across that have a count of 1
- return it's index
- return -1 after the iteration loop



"""
from collections import Counter

def first_uniq_char(s):
    counts = Counter(s)
    
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i
    
    return -1

print(first_uniq_char("leetcode"))
