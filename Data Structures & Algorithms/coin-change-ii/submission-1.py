class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        cache = {}

        def dfs(i, current):
            if current == 0:
                return 1
            
            if i >= n:
                return 0

            if (i, current) in cache:
                return cache[(i, current)]

            res = 0
            if current >= coins[i]:
                res = dfs(i + 1, current)
                res += dfs(i, current - coins[i])

            cache[(i, current)] = res
            return res
        
        return dfs(0, amount)