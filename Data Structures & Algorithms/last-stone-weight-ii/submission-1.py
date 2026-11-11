class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        maxStoneW = sum(stones)
        target = (maxStoneW + 1) // 2
        cache = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (maxStoneW - total))
            
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

            return cache[(i, total)]

        return dfs(0, 0)