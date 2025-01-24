"""
PROBLEM:
- we are given an array of strings
- we are required to find the longest common prefix among those strings
- if there is no prefix, return an empty array
input: array
output: string

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""

EDGE CASES:
empty array? ==> empty string
does case matter?  ==> No

APPROACH:
- longest common prefix that is possible is the whole first word
- so we might need to iterate over the array, at least for the length of that word
- say first word is flower, we will have to iterate over the array 6 times at most
- we get the length of the first word
- start a for loop that will run n number of times, n being length of that word
- on each iteration we go over the array and check the first letter of each word
- if it's the same, as in its the same as in the first word, we add it to the prefix variable
- and keep going, at any point, we feel like, commonality ends, we can just return the prefix
- which will be an empty variable to start with



PSEUDOCODE:
- SET prefix = ""
- shortest_word = min(arr, key=len)
- SET max_prefix_length = len(shortest_word)
- FOR LOOP for max_prefix_length number of times
    ON EACH ITERATION check the letter in all words of the array
    FOR word in the array
      if check if word[i] == shortest_word[i]s
      add to prefix
      if not
      return prefix
- 
  - 
"""

def longest_common_prefix(strs):
    prefix = ""
    shortest_word = min(strs, key=len)
    max_prefix_len = len(shortest_word)
    for i in range(max_prefix_len):
        for word in strs:
            if word[i] != shortest_word[i]:
                return prefix
        prefix += shortest_word[i]
    return prefix

print(type(longest_common_prefix(["iower","flow","flight"])))