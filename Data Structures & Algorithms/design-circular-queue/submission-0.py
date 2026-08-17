class MyCircularQueue:

    def __init__(self, k: int):
        self.storage = []
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.cap > len(self.storage):
            self.storage.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.storage) > 0:
            k = self.storage[-1]
            if k in self.storage:
                self.storage.remove(k)
                return True
        return False

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