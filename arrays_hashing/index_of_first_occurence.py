"""
PROBLEM:
- we are given two strings needle and haystack
- return the index of first occurence of needle in haystack
- or return -1 if needle doesn't exist

EXAMPLES:
needle 'a'
haystack 'sdfgsa'
output: 5

haystack 'sadbutsad'
needle 'sad'
output 0

first occurrence of sad is at index 0

leetcode
leeto
-1

- so needle can be multiple letters too
- there is no gurantee that needle would be smaller than haystack
- only consists of lowercase english letters

BREAKDOWN:
- we would need to iterate over the haystack
- on each iteration we check whether, at the current index, needle is being formed in haystack
- if it is we return that index
- but if loop finishes, we return -1
HOW?

- first we need to take into account the length of needle, if needle is 3 characters,
  on each iteration, we will have to check the 3 letters, starting from the current idx
- and we have to make sure that, current index + len of needle don't fall out of list index range either
- because as soon as they do, needle is not there, loop is finished

PSEUDO CODE:
DEF first_occurrence(haystack, needle):
    idx = 0
    size = len(needle)

    while idx + size <= len(haystack):
        if haystack[idx: idx+size] == needle:
            return idx
        
        idx += 1
    
    return - 1
"""

def first_occurrence(haystack, needle):
    idx = 0
    size = len(needle)

    while idx + size <= len(haystack):
        if haystack[idx : idx + size] == needle:
            return idx
        idx += 1

    return - 1

print(first_occurrence('leetcode', 'leeto'))