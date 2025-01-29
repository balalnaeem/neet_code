"""
PROBLEM:
- We are given a string and pattern
- we want to check whether the string follows the pattern

EXAMPLES:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

As we can see from examples that string words have to kind of map to the letters in the pattern.
And if one letter is mapped to word, and word is mapped to a letter throughout the string,
we return true.

EDGE CASES:
Would the letters in pattern be of the same length as the words in the string?
- pattern
  - would be 1 =< pattern <= 300
  - contains only lowercase letters
- string
  - would be 1 =< string <= 3000
  - string only contains letters and spaces.
  - doesn't contain any leading or trailing spaces either.
  - and contains lowercase letters.
  - a standard string (nothing edge casey)

So far it looks like string(words) and pattern(letters) length would be same. 

APPROACH:
- we need to iterate over the pattern
- we need to have a dict so we can map the letters to words
- if a letter has already been mapped, or a word has alraedy been mapped to a letter, we return false
- so we may need to have two dicts one letters to words and one words to letters so check in both on each iteration

PSEUDO CODE:
DEF word_pattern(str, pattern)
    DICT 1 letters to words mapping = {}
    DICT 2 words to letters mapping = {}

    FOR LOOP for idx in range(len(pattern)):
        IF DICT 1 has the char as key:
            check char's value is equal the word in the string at that index
            if not return false
        ELSIF DICT 2 has the word in the keys:
            if it does, check whether the value letter is the same as the current index in pattern
            if not return false
        ELSE:
            DICT 1[char] == word in the string
    return True
"""

def word_pattern(pattern, str):
    char_to_word = {}
    word_to_char = {}
    words = str.split()

    if len(words) != len(pattern):
        return False

    for idx in range(len(pattern)):
        if char_to_word.get(pattern[idx]) and not word_to_char.get(words[idx]):
            return False
        if word_to_char.get(words[idx]) and not char_to_word.get(pattern[idx]):
            return False
        if char_to_word.get(pattern[idx]) and word_to_char.get(words[idx]):
            if char_to_word.get(pattern[idx]) != words[idx]:
                return False
        else:
            char_to_word[pattern[idx]] = words[idx]
            word_to_char[words[idx]] = pattern[idx]
    
    return True

print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))