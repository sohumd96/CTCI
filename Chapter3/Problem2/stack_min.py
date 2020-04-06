class StackMin:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        val = self.stack.pop(0)
        if self.stack_min[0] == val:
            self.stack_min.pop(0)
        return val

    def push(self, ele):
        if len(self.stack_min) == 0 or self.stack_min[0] >= ele:
            self.stack_min.insert(0, ele)
        self.stack.insert(0, ele)

    def min(self):
        if len(self.stack_min) == 0:
            return None
        return self.stack_min[0]

    def get_stack(self):
        return self.stack

    def get_min_stack(self):
        return self.stack_min
