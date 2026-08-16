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
                cache[res] = 1
                res = calculate(res)
            else:
                return False
        
        return True