class Solution:
    def numSquares(self, n: int) -> int:

        def dfs(target):
            if target == 0:
                return 0
            
            res = target
            for i in range(1, target):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i*i))
            
            return res
        
        return dfs(n)