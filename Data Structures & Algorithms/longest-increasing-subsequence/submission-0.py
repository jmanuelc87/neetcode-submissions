class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0

            lis = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                lis = max(lis, 1 + dfs(i + 1, i))
            
            return lis
        
        return dfs(0, -1)