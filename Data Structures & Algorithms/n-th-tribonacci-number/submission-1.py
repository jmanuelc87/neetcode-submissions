class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        t1, t2, t3 = 0, 1, 1
        res = 0
        for i in range(n - 2):
            res = t3 + t2 + t1
            t1, t2, t3 = t2, t3, res
        return res
