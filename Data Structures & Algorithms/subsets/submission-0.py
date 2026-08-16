class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, nums, res, [])
        return res

    def dfs(self, i, nums, res, subset):
        if i >= len(nums):
            res.append(subset.copy())
            return

        self.dfs(i + 1, nums, res, subset + [nums[i]])
        self.dfs(i + 1, nums, res, subset)