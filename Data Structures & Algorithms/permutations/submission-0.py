class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(perms, nums, picks):
            if len(perms) == n:
                res.append(perms[:])
                return

            for i in range(n):
                if not picks[i]:
                    perms.append(nums[i])
                    picks[i] = True
                    dfs(perms, nums, picks)
                    perms.pop()
                    picks[i] = False

        dfs([], nums, [False] * n)

        return res