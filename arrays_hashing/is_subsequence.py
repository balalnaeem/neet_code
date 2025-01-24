"""
PROBLEM:
- We are given two strings s and t
- we need to decide whether s is a subsequence of t
- What is a subsequence?
- If we delete few (or none) letters from a string, without disturbing the position of the remaining letters,
  remaining letters string is a subsequence of the original string.
- basically, the letters that come before in the original string should also come before in the subsequence.

EXAMPLES:
Letters in t and order same
Input: s = "abc", t = "ahbgdc"
Output: true

Letter not in t
Input: s = "axc", t = "ahbgdc"
Output: false

Letters in t but the order changed
Input: s = "acd", t = "ahbgdc"
Output: false

EDGE CASES:
- where s and t are the same? Yes?
- where s is empty string? Yes?
- case sensitive? (only lower case letters)
- no space characters?

APPROACH:
- we can iterate over the subsequence
- while checking for the current letter in t
- if we can find all the letters of s in t in the same order, we have a subsequence
- but if we get to the end of t without finding all the letters of s, we return False

AL:
- iterate ove the s string
- first letter becomes the letter we are looking for
- we start iterating of the t string, looking for the target letter
- as soon as we find the target letter, target letter is set to the next letter in s string
- and we continue our iteration over the t string
- if we get to the end of s string and have found all the letters, return True
- if we get to the end of t string and have not found all the letters, return False
- that way we only iterate over the t string once, its O(n)

PSEUDO CODE:
DEF METHOD is_subsequence(s, t)
if s is empty, return True

SET target_letter_idx = 0
ITERATE over t string
    ON EACH ITERATION
    IF the current letter in t is equal to target letter
        target_letter_idx += 1
    IF target_idx >= len(s)
        return True

return False
    
input s = 'abc', t = 'abc'
output True
"""

def is_subsequence(s, t):
    if not s:
        return True
    target_index = 0
    for char in t:
        if char == s[target_index]:
            target_index += 1
        if target_index >= len(s):
            return True
    return False

s = ""
t = "acd"

print(is_subsequence(s, t))