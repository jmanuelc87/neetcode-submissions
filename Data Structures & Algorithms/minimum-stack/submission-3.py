class MinStack:
    def __init__(self):
        self.cache = []

    def push(self, val: int) -> None:
        self.cache.append(val)

    def pop(self) -> None:
        self.cache.pop()

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.cache[-1]

        while len(self.cache):
            mini = min(mini, self.cache[-1])
            tmp.append(self.cache.pop())

        while len(tmp):
            self.cache.append(tmp.pop())

        return mini