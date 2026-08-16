class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}

        def dfs(k):
            if k >= n:
                return 0

            if k in cache:
                return cache[k]

            cache[k] = cost[k] + min(dfs(k + 1), dfs(k + 2))

            return cache[k]
        
        return min(dfs(0), dfs(1))

