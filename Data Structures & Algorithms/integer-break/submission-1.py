class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {1: 1}

        for num in range(2, n + 1):
            cache[num] = 0 if num == n else num
            for i in range(1, num):
                val = cache[i] * cache[num - i]
                cache[num] = max(cache[num], val)

        return cache[n]
