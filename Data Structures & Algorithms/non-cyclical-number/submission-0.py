class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        res = n

        def calculate(r: int):
            a = str(r)
            r = 0
            for c in a:
                r += (int(c) ** 2)
            return r

        while res != 1:
            if res not in cache:
                res = calculate(res)
                cache[res] = 1
            else:
                return False
        
        return True