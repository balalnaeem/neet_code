"""
PROBLEM:
- we are given a string s
- we need to return True if the string is a palindrome
- we are allowed to delete one character from it max
- if we don't have to, we don't have to
- return False, if it is not

EXAMPLES:
"aba" ==> True

"abca" ==> True (deleted 'c')

"abc" ==> False

BREAKDOWN:
- so palindrome is a string that is read same backwards and forwards
- so basically makeup of the character is such that if start reading them from back
  it would make the same word
- in this problem, we could have one letter that is the odd one out, and we get rid of it,
  and string is still palindrome, we return True
- How do we get to that letter?
- we can start by reading the string from both sides
- start and end
- from start we move forward, from end we move in
- if at any point, we come across a letter that's not equal to the next letter at opposite side,
  we ignore it and move forward?
- But the question is form which side's should we move to the next bit?
- from here we would need to check, whether the next letter from left or right are the equal to the opposite side
  coz that would be the app next letter
- a bit of conditional logic in that point
- if even next one is not equal from both sides, we return False
- or if we come across a 2nd not equal, we return False
- so basically we keep track of how many anomalies we have come across

TWO POINTER APPROACH:

DEF valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            anomalies += 1
            if anomalies > 1:
                return False
            if s[left + 1] == s[right]:
                left += 1
            elif s[right - 1] == s[left]:
                right -= 1
            continue
        left += 1
        right -= 1
    
    return True


acbaabcaaba
"""
def valid_palindrome(s):
    l, r = 0, len(s) -1

    while l < r:
        if s[l] != s[r]:
            skip_l = s[l + 1 : r + 1]
            skip_r = s[l : r]
            return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
        l += 1
        r -= 1
    return True

print(valid_palindrome('"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"'))

