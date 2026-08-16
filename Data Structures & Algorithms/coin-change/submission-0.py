class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(a):
            if a == 0:
                return 0

            if a in cache:
                return cache[a]
            
            res = 1e9
            for coin in coins:
                if a - coin >= 0:
                    res = min(res, 1 + dfs(a - coin))

            cache[a] = res
            return res
        
        min_coins = dfs(amount)
        return -1 if min_coins >= 1e9 else min_coins