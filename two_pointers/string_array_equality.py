"""
PROBLEM:
- we are given two string arrays
- if they represent the same string altogether
- return True, False otherwise

"""

def array_strings_equal(word1, word2):
    return ''.join(word1) == ''.join(word2)

# space saving approch

def array_strings_equality(word1, word2):
    i, j, w1, w2 = 0, 0, 0, 0
    
    while i < len(word1) and j < len(word2):
        if word1[i][w1] != word2[j][w2]:
            return False
        
        w1 += 1
        w2 += 1

        if len(word1[i]) == w1:
            i += 1
            w1 = 0
        
        if len(word2[j]) == w2:
            j += 1
            w2 = 0
    
    return i == len(word1) and j == len(word2)
