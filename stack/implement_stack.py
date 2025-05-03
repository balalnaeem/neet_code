"""
PROBLEM:
- implement a LIFO stack using only two queues
- stack should support all normal functions: push, top, pop, empty

push(int) - should push the int to the top of the stack (return null)
pop()     - remove the element at the top of the stack (return int)
int()     - return element at the top of the stack (return int)
empty()   - return True or False depending on if the stack is empty


"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        
    def push(self, x):
        self.q.append(x)
        
    def pop(self):
        for _ in range(len(self.q) -1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]
        
    def empty(self):
        return len(self.q) == 0
    


my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
top = my_stack.top()
popped = my_stack.pop()
empty = my_stack.empty()
top = my_stack.top()

print(top, popped, empty, top)