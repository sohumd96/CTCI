class SetOfStacks:
    def __init__(self, stack_limit):
        self.stack_set = [[]]
        self.stack_number = 0
        self.stack_limit = stack_limit

    def push(self, ele):
        if len(self.stack_set[self.stack_number]) == self.stack_limit:
            self.stack_set += [[ele]]
            self.stack_number += 1
        else:
            self.stack_set[self.stack_number] += [ele]

    def pop(self):
        if self.stack_set[self.stack_number] == 0:
            return None
        val = self.stack_set[self.stack_number].pop()
        if len(self.stack_set[self.stack_number]) == 0 and len(self.stack_set) != 1:
            self.stack_set.pop()
            self.stack_number -= 1
        return val

    def pop_at(self, i):
        if i >= len(self.stack_set) or len(self.stack_set[0]) == 0:
            return None
        if i == self.stack_number:
            val = self.stack_set[i].pop()
            if len(self.stack_set[self.stack_number]) == 0:
                self.stack_set.pop()
            return val
        val = self.stack_set[i].pop()
        for x, y in zip(range(i, len(self.stack_set) - 1), range(i + 1, len(self.stack_set))):
            for j in range(len(self.stack_set[x]), self.stack_limit):
                self.stack_set[x] += [self.stack_set[y].pop(0)]
        if len(self.stack_set[-1]) == 0 and len(self.stack_set) != 1:
            self.stack_set.pop()
        return val

    def get_stack(self):
        return self.stack_set
