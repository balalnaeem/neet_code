"""
PROBLEM:
- our file system keeps a log each time some user performs a change-folder operation
- operations are described as following:
  (../) - move to the parent folder of the current folder
          if you are already in the main folder, no change
  (./) - remain in the same folder
  (x/) - move to the child folder of the name x (x is guaranteed to exist)

- we are given a list of operations performed by the user
- we always start in the main folder

- we need to return the min operations needed to go back to the main folder
  after all the operations in the given list are performed

EXAMPLES:
input: logs = ["d1/","d2/","../","d21/","./"]
output: 2

input: logs = ["d1/","d2/","./","d3/","../","d31/"]
output: 3

input: logs = ["d1/","../","../","../"]
output: 0

BREAKDOWN:
- we always starting in the main folder
- we can use a stack here to keep a record of how many folders deep we are at any given point
- and that would be the number of ops needed to get back to main
- ../ would pop the latest from stack, if any exists, if it doesn't it would mean, we are already in the main folder
  so don't need to do anything
- ./ would mean do nothing
- x/ would add that to the stack, which means we are now one layer down

"""

def min_ops(logs):
    stack = []
    for op in logs:
        if op == '../' and len(stack) > 0:
            stack.pop()
        elif op == './' or op == '../':
            continue
        else: 
            stack.append(op)
    
    return len(stack)

print(min_ops(["./","../","./"]))

# better space complexity

def min_ops(logs):
    depth = 0
    for op in logs:
        if op == "../":
            if depth > 0:
                depth -= 1
        elif op != "./":
            depth += 1
    return depth
        