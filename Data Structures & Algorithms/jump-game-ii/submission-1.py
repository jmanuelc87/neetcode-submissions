class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res, l, r = 0, 0, 0

        while r < n - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            res += 1
        
        return res