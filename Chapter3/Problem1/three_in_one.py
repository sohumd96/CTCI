class three_stack:
    def __init__(self):
        self.stack = [None] * 3
        self.s1 = 0
        self.s2 = 1

    def pop(self, stack):
        if stack == 1:
            val = self.stack.pop(0) if self.stack[0] is not None else None
            self.s1 -= 1
            self.s2 -= 1
        elif stack == 2:
            val = self.stack.pop(self.s1+1) if self.stack[self.s1+1] is not None else None
            self.s2 -= 1
        elif stack == 3:
            val = self.stack.pop(self.s2+1) if self.stack[self.s2+1] is not None else None
        return val

    def push(self, stack, ele):
        if stack == 1:
            self.stack.insert(0, ele)
            self.s1 += 1
            self.s2 += 1
        elif stack == 2:
            self.stack.insert(self.s1+1, ele)
            self.s2 += 1
        elif stack == 3:
            self.stack.insert(self.s2+1, ele)

    def peek(self, stack):
        if stack == 1:
            val = self.stack[0] if self.stack[0] is not None else None
        elif stack == 2:
            val = self.stack[self.s1+1] if self.stack[self.s1+1] is not None else None
        elif stack == 3:
            val = self.stack[self.s2+1] if self.stack[self.s2+1] is not None else None
        return val

    def is_empty(self, stack):
        return True if self.peek(stack) is None else False
