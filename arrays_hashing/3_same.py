"""
PROBLEM:
- we are given a string of integers
- we need to return the maximum good integer as a string or return an empty string
  if no max good integer exists

What is a good integer?
- it is a substring of the input string with length of 3
- It consists of only 1 unique digit
- so 3 consecutive letters that are them same digit

EXAMPLES:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

Approach:
- if we just want to go over the string once, we can compare on each iteration
- but problem would come for the last 3 digits
- we can add temporary letters at the end to extend the string
- or only do the loop for 2 less than the length
- few way it can be done
- every time we find the good number, we need to check if we already found one,
- if we did, we compare them, whichever is the bigger, we keep that one
"""

def largest_good_integer(num):
    good_integers = []

    for i in range(len(num) - 2):
        sliced_3 = num[i:i+3]
        if all(c == sliced_3[0] for c in sliced_3):
            good_integers.append(sliced_3)
    return max(good_integers, key=int) if len(good_integers) > 0 else ""


print(largest_good_integer("6777133339"))