class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}

        def dfs(target):
            if target == 0:
                return 0

            if target in cache:
                return cache[target]
            
            res = target
            for i in range(1, target):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i*i))
            
            cache[target] = res

            return cache[target]
        
        return dfs(n)