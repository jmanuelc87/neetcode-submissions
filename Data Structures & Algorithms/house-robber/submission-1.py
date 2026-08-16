class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}

        def dfs(i):
            if i >= n:
                return 0
            
            if i in cache:
                return cache[i]

            res = max(nums[i] + dfs(i + 2), dfs(i + 1))

            cache[i] = res

            return cache[i]

        return dfs(0)