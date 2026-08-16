class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, current, picks):
            if len(current) == len(nums):
                res.append(current.copy())

            for i, n in enumerate(nums):
                if picks[i]:
                    continue
                
                if i and nums[i] == nums[i - 1] and not picks[i - 1]:
                    continue
                
                current.append(n)
                picks[i] = True
                dfs(i + 1, current, picks)
                picks[i] = False
                current.pop()
        
        dfs(0, [], [False] * len(nums))

        return res