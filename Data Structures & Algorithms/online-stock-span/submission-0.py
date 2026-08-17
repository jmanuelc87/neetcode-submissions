class StockSpanner:

    def __init__(self):
        self.stack  = []
        self.i = 1

    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-res][1]:
            res += 1

        self.stack.append((self.i, price))
        self.i += 1

        print(self.stack)

        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

