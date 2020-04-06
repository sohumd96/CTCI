class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, ele):
        self.s1 += [ele]

    def dequeue(self):
        if len(self.s2) > 0:
            return self.s2.pop()
        elif len(self.s1) > 0:
            while self.s1:
                self.s2 += [self.s1.pop()]
            return self.s2.pop()
        else:
            return None
