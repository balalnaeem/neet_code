"""
PROBLEM:
- we are given a string of 0's and 1's
- we need to transfor it into an alternating string
- using minimum operations of changing 0's to 1's or vice versa

EXAMPLES:
input: "0100"
output: 1
We only need to transform the last 0 to 1 to turn the string into "0101"

input: "10"
output: 0
no operations are needed

input: "1111"
outpu: 2

The tricky part is "minimum operations"
An example where it's possible to use not minimum operations:
3 ops
00100
01010

2 ops
00100
10101
-----------
4 ops
000001
101010

2ops
000001
010101
------------
5 ops
000010000
010101010

4ops
000010000
101010101
------------
6ops
000111000
101010101

3ops
000111000
010101010
------------
6ops
111000111
010101010

3ops
111000111
101010101

Seems like we have to do 2 iterations over the string
one starting with 0's and one starting with 1's
Doesn't seem very efficient though
But lets implement it anyway
we iterate over the string
on each letter check the previous letter, if it's the same, we replace the current letter with
the opposite

we do the iteration twice, once starting with 0 and once starting with 1
since these are the only two options

"""

def min_operations(s):
    count = 0 # number of ops if we start with 0

    for i in range(len(s)):
        if i % 2: # odd
            count += 1 if s[i] == "0" else 0
        else: # even
            count += 1 if s[i] == "1" else 0
    
    return min(count, len(s) - count)
    