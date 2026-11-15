class MinStack:
    def __init__(self):
        self.cache = []
        self.mini = []

    def push(self, val: int) -> None:
        self.cache.append(val)
        val = min(val, self.mini[-1] if self.mini else val)
        self.mini.append(val)

    def pop(self) -> None:
        self.cache.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        return self.mini[-1]
