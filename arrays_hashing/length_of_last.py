"""
PROBLEM:
- we are given a string of words and spaces.
- we are required to return the length of last word
- a word is consisting of non-space characters

EXAMPLES:
Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Input: s = "luffy is still joyboy"
Output: 6

EDGE CASES:
empty string? Nope
s has only english letters and spaces.
There will at least be one word in s.
periods count? We won't have periods.

APPROACH:
- we can split the string on whitespace
- get the last word and return it's length

"""

def length_of_last(str):
  return len(str.split()[-1])