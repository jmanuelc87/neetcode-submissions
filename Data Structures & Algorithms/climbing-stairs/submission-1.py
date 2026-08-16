class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n


        one, two, res = 1, 1, 0

        for i in range(n - 2, -1, -1):
            res = one + two
            two = one
            one = res

        return res