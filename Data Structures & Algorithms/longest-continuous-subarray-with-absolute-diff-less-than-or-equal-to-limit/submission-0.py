class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = res = 0

        for r in range(len(nums)):

            while abs(nums[l] - nums[r]) > limit:
                l +=1

            res = max(res, r - l + 1)

        return res