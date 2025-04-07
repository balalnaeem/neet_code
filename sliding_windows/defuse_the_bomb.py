"""
PROBLEM:
- we are given an array of integers, code
- we are given an integer, k
- we have to replace every integer in the array code
- replacement should happen according to the following conditions:
  1. if k > 0, replace the integer with the next k numbers
  2. if k < 0, replace the integer with the prev k numbers
  3. if k == 0, replace the integer with 0
- return the replaced array or decrypted code

EXAMPLES:
in: [5, 7, 1, 4], k = 3
out: [12, 10, 16, 13]

in: [2, 4, 9, 3], k = -2
out: [12, 5, 6, 13]

in: [1, 2, 3, 4], k = 0
out: [0, 0, 0, 0]

BREAKDOWN:
- we need to create a circular window for the array
- if the next element is out of reach of the array, we go to the beginning of the array
- if the next element's index is greater than or equal to array's length, array len - the index will be the accurate index
- but if we are checking the previous elements, current index - 1, - 2 - 3 and that will take care of itself

APPROACH:
- DEF decrypt method, args = code, k
- initialize result empty array
- iterate over the given array of integers with index
- at each index preform the following action
  - start a loop that iterates k(3) number of times
  - if k is + loop with go for 1 to 3
  - if k is - loop will go for -1 to -3
  - if k is 0 loop will still go three times but no need for any calculations
  - and on each iteration find the next k numbers and and add them up and insert sum into the result array
- return result array
-
"""

def decrypt(code, k):
    code_len = len(code)

    if k == 0:
        return [0] * code_len
    
    result = []
    
    for i in range(code_len):
        temp = 0
        if k > 0:
            for j in range(1, k + 1):
                idx = i + j
                if idx >= code_len:
                    idx = idx - code_len
                temp += code[idx]
        else:
            for j in range(-1, k - 1, -1):
                idx = i + j
                temp += code[idx]
        
        result.append(temp)
    
    return result

print(decrypt([2, 4, 9, 3], 0))