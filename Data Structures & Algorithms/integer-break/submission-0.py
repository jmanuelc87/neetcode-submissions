class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {1:1}

        def dfs(num):
            if num in cache:
                return cache[num]
            
            cache[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                cache[num] = max(cache[num], val)

            return cache[num]

        return dfs(n)
