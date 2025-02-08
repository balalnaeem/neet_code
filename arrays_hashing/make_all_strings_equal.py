"""
PROBLEM:
- we are given an array of strings
- return True if you can make all strings in the list equal by moving letters between different strings
- False otherwise

EXAMPLES:
Input: words = ["abc","aabc","bc"]
Output: true

Input: words = ["ab","a"]
Output: false

EDGE CASES:
single letter strings
['a', 'b', 'c']

different strength of different letters
['abbccc', 'aabbccc', 'bbccc']
abbccc
abbccc
abbccc

one string list
['a']

- list will have at least one word in it
- all words will have at least one letter in them
- all words have lowercase english letters

 

"""
from collections import Counter

def make_equal(words):
    all_words = "".join(words)
    char_count = Counter(all_words)
    
    for c in char_count:
        if char_count[c] % len(words):
            return False
    
    return True




