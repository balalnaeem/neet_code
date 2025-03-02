"""
PROBLEM:
- we are given an array of strings
- we have to return the first palindromic string
- if there is no such string, we return an empty string

EXAMPLES:
in: ["abc","car","ada","racecar","cool"]
out: "ada"

in: ["notapalindrome","racecar"]
out: racecar

in: ["def","ghi"]
out: ""

- no empty array
- no empty string
- only lowercase english letters

BREAKDOWN:
- Problem is two step problem
- first we need logic to decide whether a string a palindromic string
- then we need to iterate over the array and return the first string we come across that is palindromic
- we can find out if a string is palindromic with 
"""

def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    
    return ""

