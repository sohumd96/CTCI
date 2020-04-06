class SortStack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, ele):
        while self.stack and self.peek() < ele:
            self.temp += [self.pop()]
        self.stack += [ele]
        while self.temp:
            self.stack += [self.temp.pop()]

    def peek(self):
        return self.stack[-1] if self.stack else None

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
