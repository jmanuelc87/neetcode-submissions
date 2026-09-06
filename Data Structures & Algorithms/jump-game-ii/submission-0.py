class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == n - 1:
                return 0

            if nums[i] == 0:
                return float('inf')

            res = float('inf')
            end = min(n, i+nums[i]+1)
            for j in range(i+1, end):
                res = min(res, 1 + dfs(j))

            cache[i] = res
            return res

        return dfs(0)