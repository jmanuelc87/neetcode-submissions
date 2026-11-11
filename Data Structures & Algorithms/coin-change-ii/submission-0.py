class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}

        def dfs(i, current):
            if current == 0:
                return 1
            
            if i >= n:
                return 0

            if (i, current) in cache:
                return cache[(i, current)]

            cache[(i, current)] = 0
            if current >= coins[i]:
                cache[(i, current)] = dfs(i + 1, current)
                cache[(i, current)] += dfs(i, current - coins[i])

            return cache[(i, current)]
        
        return dfs(0, amount)