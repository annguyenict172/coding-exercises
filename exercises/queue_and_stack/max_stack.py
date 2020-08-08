"""
Stack with Max API: EPI 8.1
"""


class Stack(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.max_stack) == 0 or self.max_stack[-1] < val:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def max(self):
        return self.max_stack[-1]


# Test with Stack [1,-1,-2,3,-5,10]
stack = Stack()
stack.push(1)
stack.push(-1)
stack.push(-2)
stack.push(3)
stack.push(-5)
stack.push(10)

assert stack.max() == 10
stack.pop()
assert stack.max() == 3
stack.pop()
assert stack.max() == 3
stack.pop()
assert stack.max() == 1
