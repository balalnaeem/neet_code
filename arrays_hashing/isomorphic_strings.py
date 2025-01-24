"""
PROBLEM:
- given two strings, s and t
- find out if they are isomorphic

What is isomorphic?
- if you replace the letters of one string, you can get the other string
- one letter could only be replaced by one other letter

EXAMPLES:
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true

EDGE CASES:
- case sensitive?
No need to account for the case
- characters can map to themselves?
Yes
- one character can only be mapped to one other character

APPROACH:
- we can start iterating over the letters in string s
- on each iteration, we can save the equivalent letter in the t string in a dictionary
- so on each iteration we need to check if the letter in s string has already been
  mapped to another string:
    - if it is, we need to check that the letter it's been mapped to is the same as the current
    letter in string t
    - if it is not, we map it to the current letter in the string t
      - but before we do that, we need to check if the current letter in string t has already been mapped
      - if it is we return false
      - if not, we map the letter in s string to the current letter in t string

How can we have a dict return None, if the we are checking for key that doesn't exist?
I think we dict.get('a') 

"""

def is_isomorphic(s, t):
  s_to_t = {}
  t_to_s = {}
  for letter_s, letter_t in zip(s, t):
      if ((letter_s in s_to_t and s_to_t[letter_s] != letter_t) or
            (letter_t in t_to_s and t_to_s[letter_t] != letter_s)):
         return False
      else:
         s_to_t[letter_s] = letter_t
         t_to_s[letter_t] = letter_s

  return True

print(is_isomorphic('badc', 'baba'))