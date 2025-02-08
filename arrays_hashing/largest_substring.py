"""
PROBLEM:
- we are given a string
- we need to return the length of longest substring between two same characters
- even if the substring is an empty string, we return it's length, which is 0
- if there is no such substring, there is no repeating characters, return -1

EXAMPLES:
Input: s = "aa"
Output: 0

Input: s = "abca"
Output: 2

Input: s = "cbzxy"
Output: -1

EDGE CASES:
- there can be multiple substrings
'abcdabcdfa'
4 should be the output

- there can be multiple substrings between different letters
'agggackkkkkc'
5 output because of the 5 k's between c's

BREAKDOWN:
- this will ofcourse be another problem of looping over the string
- although on each iteration we need to keep track of the number of letters
- and if a letter gets repeated, means there is possible substring between the repetition
Stuff to think about?
- How to keep count of letters?
- How to know when you come across a repeate letter?
- How to count the substring in between the same chars?
- How to continue looking for the longest substring after calculating one?

- we can use a hashmap to store the letters
- if at any point we see this letter already exists, we count the letters traversed so far
  excluding the previous iteration of the same letter
- after saving the count in a variable, we continue our traversal from the current letter (meaning the repeat letter we came across) because that could make some other substring
- and since the next substring could be made by different letters, we need to keep track of index of each letter
- when a repeat character comes, after calculating the possible substr len, it's index gets updated of course

APPROACH:
- we will set a variable to an empty hasmap or perhaps a defaultdict with int 0
- we will set another varibale max_substr_len and set it to 0
- we will start a loop and iterate over the string
- on each iteration, we will check first whether the current letter has been repeated / already exists in the hashmap.
  if No:
    - we save the letter in the hash as key and it's index as value
  if Yes:
    - we take its index and add 1 to it. And then subtract it from the current index
    - we check whether this answer is greater than max_susbstr_len, 
          if it is, we set it equal to that new number
          if it is not, we leave it as is
    - and then we update the index of the current letter

PSEUDO CODE:
DEF max_length_between_equal_characters(s):
    SET char_indices = {}
    SET max_substr_len = -1

    LOOP for i in range(len(s)):
        if s[i] in char_indices:
            cur_substr_len = i - char_indices[s[i]] + 1
            max_len = max(cur_len, max_len)
            char_indices[s[i]] = i
        else:
            char_indices[s[i]] = i
    
    return max_substring_len

"abca"
"""
def max_len_between_equal_chars(s):
    char_indices = {}
    max_substr_len = -1

    for idx in range(len(s)):
        char = s[idx]
        if char in char_indices:
            cur_substr_len = idx - (char_indices[char] + 1)
            max_substr_len = max(cur_substr_len, max_substr_len)
        else:
            char_indices[char] = idx
    
    return max_substr_len

print(max_len_between_equal_chars("mgntdygtxrvxjnwksqhxuxtrv"))
