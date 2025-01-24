"""
PROBLEM:
- we are given an array of integers
- we need to replace every element, with the greatest element to the right
- so at each index, we need to replace the current index integer with 
  any integer at the following indices which is the greatest
- And the last element, will get replaced by -1
- And we return the result array

EXAMPLES:

input: [17,18,5,4,6,1]
ouput: [18,6,6,6,1,-1]

input: [400]
outpu: [-1]

- if there is only one element, we just return that replaced with -1
- that makes sense

APPROACH:
- we need iterate over the array, while appending the max from following indices to the result array
- so initialize a result array
- iterate over the input array with indices
- on each iteration, 
    - another iteration willt take place, where we will check the value at the following indices
      and identify the max
- after the inner iteration, we append the max to the result array
- when we are at the last index, we just append -1 to the array
- we can also save the index of the max, and keep replacing the values until we are that index
- this way we will save the iteration where the max is going to stay the same

PSEUDO CODE:
DEF replace_elements(arr):
    last_idx = len(arr) - 1
    max_val_idx = 0

    FOR idx in range(last_index):
        IF max_value_index == idx:
            FOR i in range(idx + 1, last_index + 1, step= 1):
                if arr[i] > arr[max_val_idx]:
                  max_val_idx = i
        arr[idx] = arr[max_val_idx]
    arr[last_idx] = -1
    return arr
"""

def replace_element(arr):
    last_idx = len(arr) - 1
    max_val_idx = 0

    for idx in range(last_idx):
        if max_val_idx == idx:
            max_val_idx += 1
            for new_max_idx in range(max_val_idx, last_idx + 1):
                if arr[new_max_idx] > arr[max_val_idx]:
                    max_val_idx = new_max_idx
        arr[idx] = arr[max_val_idx]
    arr[last_idx] = -1
    return arr

arr = [17,18,5,4,6,1]
print(replace_element(arr))