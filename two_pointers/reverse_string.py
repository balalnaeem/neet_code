"""
PROBLEM:
- we are given an array of chars
- we need to reverse that array in place
- no need to return anything, just modify the array.

EXAMPLES:
["h","e","l","l","o"] ==> ["o","l","l","e","h"]
['H', 'a', 'n', 'n', 'a', 'h'] ==> ['h', 'a', 'n', 'n', 'a', 'H']

- no empty string.
- this reversal should happen in place

BREAKDOWN:
- since we have to modify the array in place
- we can iterate over the array while appending each letter to the front of the array
- that way we have the first half of the array as reversed of the second half and then
we just del the second half starting from the original arr len

['h', 'e', 'l', 'l', 'o']
1st iteration
['h', 'h', 'e', 'l', 'l', 'o']
2nd iteration
['e', 'h', 'h', 'e', 'l', 'l', 'o']
....
final iteration
['o', 'l', 'l', 'e', 'h', 'h', 'e', 'l', 'l', 'o']

after deletion
['o', 'l', 'l', 'e', 'h']


"""

def reverse_string(s):
    copy = s[::-1]
    for item in copy:
        s.append(item)
    del s[0:len(copy)]

arr = ['h', 'e', 'l', 'l', 'o']
reverse_string(arr)
print(arr)