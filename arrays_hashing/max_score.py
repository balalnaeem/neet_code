"""
PROBLEM:
- We are given a string of 0's and 1's
- we need to return the maximum score possible
- score is calculated after splitting the string in two
  count the 0's from left half
  count the 1's from right half
- so we basically need to split the string at the point where the score would be max
  i.e. max 0's on the left half and max 1's on the right half
- string must be split into 2 non empty strings


EXAMPLE:
Input: s = "011101"
Output: 5 

All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Input: s = "1111"
Output: 3

APPROACH:
- we have to split the string into two non empty strings
- so we can split after index 0 and before the last index
- '0 1 1 1 0 1'

- so we would need to iterate over the string twice
- first we would need to iterate just to count the number of 1
  so we can use the count method
- then the second iteration is the really important one because that decide the score on each iteration
- so initialize varibale to keep the score of 1's
- set the score of 0's to zero
- set the max score to negative inifinity
- and start the iteration
  - on each iteration if the current element is 0, add the 1 to the zero score
  - if the current element is 1, minus 1 from the one's score
  - after that's done, calculate the current max score
  - if the current max score is greater than the previous max score, set the max score to the new max
- once iteration is finished, return the max score

PSEUDO CODE:
DEF max_score(s):
    SET count_1s = s.count('1')
    SET count_0s = 0
    SET max_score = float('-inf')

    FOR char in s:
        IF char == '0':
            count_0s += 1
        IF char == '1':
            count_1s -= 1
        cur_max_score = count_0s + count_1s
        IF cur_max_score > max_score:
            max_score = cur_max_score
    
    return max_score
"""

def max_score(s):
    count_1s = s.count('1')
    count_0s = 0
    max_score = float('-inf')

    for i in range(len(s) - 1):
        if s[i] == '0':
            count_0s += 1
        if s[i] == '1':
            count_1s -= 1
        cur_max_score = count_0s + count_1s
        if cur_max_score > max_score:
            max_score = cur_max_score
    
    return max_score

print(max_score('00'))