class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        res = n

        def calculate(r: int):
            a = str(r)
            r = 0
            for c in a:
                r += int(c) ** 2
            return r

        while res != 1:
            if res not in cache:
                cache.add(res)
                res = calculate(res)
            else:
                return False

        return True
