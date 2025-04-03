"""
PROBLEM:
- we are keeping score of a baseball game with certain rules
- start with an empty record
- we are given a list of strings which are operations that need to be performed
Operations:
x = record a new score (sum of prev two scores)
D = record a new score that is double of the previous score
C = Invalidate the previous score

- we have to return sum of all the scores after all the operations have been applied

EXAMPLES:
in: ["5","2","C","D","+"]
out: 30
[5]
[5, 2]
[5]
[5, 10]
[5, 10, 15]
5 + 10 + 15
= 30

in: ["5","-2","4","C","D","9","+","+"]
out: 27

in: ["1", "C"]
out: 0

NO APPARENT EDGE CASES

APPROACH:
- iterate over the operations, on each iteration preforming the required operation on the scores array
- start of with an empty scores array
- if else statement in loop
- return the sum of score array in the end

Questions:
- how to turn array into an integers
- how to sum the array of integers
"""

def cal_points(operations):
    scores = []
    for op in operations:
        if op == 'C':
            scores.pop()
        elif op == 'D':
            scores.append(scores[-1] * 2)
        elif op == '+':
            scores.append(scores[-1] + scores[-2])
        else:
            scores.append(int(op))
    
    return sum(scores)


print(cal_points(["5","2","C","D","+"]))
print(cal_points(["5","-2","4","C","D","9","+","+"]))