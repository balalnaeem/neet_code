"""
PROBLEM:
- implement FIFO queue using only two stacks
- with the following fuctions

push - pushes element to the back of the queue
pop - removes element from the front of the queue
peek - returns the element at the front of the queue
empty - return true if the queue is empty, false otherwise


"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return popped

    def peek(self):
        return self.stack1[0]

    def empty(self):
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
popped = obj.pop()
top = obj.peek()
empty = obj.empty()

print(popped, top, empty)