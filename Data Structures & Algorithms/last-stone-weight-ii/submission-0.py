class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        maxStoneW = sum(stones)
        target = (maxStoneW + 1) // 2
        cache = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (maxStoneW - total))
            return min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

        return dfs(0, 0)