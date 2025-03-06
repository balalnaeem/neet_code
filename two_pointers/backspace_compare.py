"""
PROBLEM:
- we are given two string s and t
- return true if they are equal
- but take into account the # symbol in the string
- # means backspace character, meaning previous character doesn't exist

EXAMPLES:
in: s = "ab#c", t = "ad#c"
out: true

in: s = "ab##", t = "c#d#"
out: true
as both string would be empty

in: s = "a#c", t  = "b"
out: false

BREAKDOWN:
- so we have to iterate over the string while comparing their letters
- we can either finalize them first and then compare or compare as we iterate over them
- comparing as we iterate over them seems a little bit complicated
- how will each approach work?
1.
  - we iterate over the string array and filter it takeing out the # signs and join
  - then compare both strings
  - not the most efficient one
2.
  - we have two pointers for both string
  - on each step, check if the string has # at the next step
  - if the string does, we move forward one step and ignore the current letter
  but this can cause problems with consecutive # signs
  "ab##" a would still get compared even though in the final string it shouldn't get counted
Or 
3. 
- maybe we use two pointers for each string first
- since strings are immutable, we will need to build new strings
- convert the s into an array
- we can iterate over the array and replace every # and previous character with the ""
- then join the strings in the end
- and then compare both the final strings

CODE:
DEF backspace_compare(s, t):
    s_list = list(s)
    t_list = list(t)

    for i in range(len(s_list)):
        if s_list[i] == '#'
            s_list[i] = ''
        if i > 0:
            s_list[i - 1] = ''
    
    for i in range(len(t_list)):
        if t_list[i] == '#'
            t_list[i] == ''
        if i > 0:
            t_list[i -1] = ''
    
    return ''.join(s_list) == ''.join(t_list)

AL:
"""

def backspace_compare(s, t):
    filtered_s = []
    filtered_t = []

    for char in s:
        if char == "#":
            if filtered_s:
                filtered_s.pop()
        else:
            filtered_s.append(char)
        
    for char in t:
        if char == "#":
            if filtered_t:
                filtered_t.pop()
        else:
            filtered_t.append(char)
    
    return ''.join(filtered_s) == ''.join(filtered_t)
          
            
            


print(backspace_compare("y#fo##f","y#f#o##f"))