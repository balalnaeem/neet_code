"""
PROBLEM:
- you are given an array of string and a string (chars)
- a string is good if it can be formed by the characters of chars
- each char in chars can only be used once
- return the sum of lengths of all good strings in the array

EXAMPLES:
- Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

APPROACH:
- we have to compare the letters in each word in the array with the letters in chars
- and since each char can only be used once, it adds a complication
- it means we can't use the in operator to check
- we need to count the letters in words in array and count the ones in char
- if char don't have all the ones in words, it's not a good string
- if chars have all the letters in the word from array, it's a good string
"""

from collections import Counter


def count_characters(words, chars):
    count = Counter(chars)
    sum = 0

    for word in words:
        cur_word = Counter(word)
        good = True
        for letter in cur_word:
            if cur_word[letter] > count[letter]:
                good = False
                break
        if good:
            sum += len(word)
    return sum
            


print(count_characters(["cat","bt","hat","tree"], "atach"))