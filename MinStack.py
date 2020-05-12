# [1, 2, 3, 4, 5]

class MinStack():

    def __init__(self):
        import collections
        self.stack = collections.deque()
        self.min_list = collections.deque()
    
    def push(self, x):
        if not self.min_list or x <= self.min_list[-1]:
            self.min_list.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_list[-1]:
            self.min_list.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_list[-1]


minStack = MinStack()
minStack.push(-2)
print("Push " + str(minStack.stack) + " " + str(minStack.min_list))
minStack.push(0)
print("Push " + str(minStack.stack) + " " + str(minStack.min_list))
minStack.push(-3)
print("Push " + str(minStack.stack) + " " + str(minStack.min_list))

print("Min" + str(minStack.getMin()))
print("Pop" + str(minStack.pop()))
print("Top" + str(minStack.top()))
print("Min" + str(minStack.getMin()))
