"""
PROBLEM:
- we are given a string of words
- we have to reverse the letters in each word
  while preserving the order words originally in placer
- string will have at least one word
- no leading or trailing whitespaces
- all words are separated by a single space

EXAMPLES:
in: "Let's take leetcode contest"
out: "s'teL ekat edoCteeL tsetnoc"

in: "Mr Ding"
out: "rM gniD"

BREAKDOWN:
- we can split the string on whitespaces
- iterate over that array
- on each iteration reverse the string
- and then join the array into one string with " "
This seems simple enough, but not sure if it is efficient


"""

def reverse_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)

print(reverse_words("Let's take leetcode contest"))