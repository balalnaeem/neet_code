"""
PROBLEM:
- we are given two strings word1 and word2
- merge the strings by adding letters in alternating order
- start with word1
- if one string is longer than the other, append the remaining letters to the end

Examples:
input: 'abc', 'pqr'
output: apbqcr'

input: 'ab', 'pqrs'
output: 'apbqrs'


input: 'abcd', 'pq'
output: 'apbqcd'

- words only consist of lowercase english letters
- word will have at least one letter

Breakdown:
It's a problem of iterating over two string simultaneously
- we can have one pointer that works as index for both words
- pick letters alternately from each work and keep adding to the result word
- we can either continue this alternation, conditional on index being valid, or can slice the larger word

AL:
- set a result variable to an empty string
- set a pointer to 0 so we can start with the first letter
- start a while loop
    while pointer is < len(word1) and pointer < (word2)
        if pointer < len(word1):
            result += word1(pointer)
        if pointer < len(word2)
            result += word2(pointer)
        pointer += 1
  return the result string


  
'abc', 'pqr'

"""

def merge_alternately(word1, word2):
    merged = []
    idx = 0

    while idx < len(word1) or idx < len(word2):
        if idx < len(word1):
            merged.append(word1[idx])
        if idx < len(word2):
            merged.append(word2[idx])
        idx += 1
    
    return ''.join(merged)

print(merge_alternately('ab', 'pqrs'))