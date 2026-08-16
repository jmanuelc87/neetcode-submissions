class MyQueue:

    def __init__(self):
        self.backbone = []

    def push(self, x: int) -> None:
        self.backbone.append(x)

    def pop(self) -> int:
        x = self.backbone[0]
        del self.backbone[0]
        return x

    def peek(self) -> int:
        return self.backbone[0]

    def empty(self) -> bool:
        return len(self.backbone) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()