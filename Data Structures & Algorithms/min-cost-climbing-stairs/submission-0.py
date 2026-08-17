class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(k):
            if k >= n:
                return 0
            
            return cost[k] + min(dfs(k + 1), dfs(k + 2))
        
        return min(dfs(0), dfs(1))

