"""
PROBLEM:
- we are given an array
- we need to group the anagrams together and return a 2 dimensional array

EXAMPLE:
- Input: strs = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

APPROACH:
- first we need to create a hash to save the grouped anagrams in
- We can iterate over the array
  - and for each string, we sort it, save it in hash as key, and store the string in an array as value
  - so on each iteration we check whether the sorted string exists in the hash a key,
  - if it does we just append the string to the value
  - if not, we create a new string and set that as value
- once iteration is done, we return all values of hash
"""

def group_anagrams(strs):
    group = {}
    for str in strs:
        key = ''.join(sorted(str)) 
        if group.get(key) is None:
            group[key] = [str]
        else:
            group[key].append(str)
    
    return list(group.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))