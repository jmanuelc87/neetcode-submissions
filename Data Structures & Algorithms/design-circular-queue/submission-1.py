class MyCircularQueue:

    def __init__(self, k: int):
        self.storage = [] * k
        self.cap = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.storage[self.rear] = value
        self.size += 1

    def deQueue(self) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k

    def Front(self) -> int:
        if len(self.storage) == 0:
            return -1
        return self.storage[0]

    def Rear(self) -> int:
        if len(self.storage) == 0:
            return -1
        return self.storage[-1]

    def isEmpty(self) -> bool:
        return len(self.storage) == 0

    def isFull(self) -> bool:
        return len(self.storage) == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()