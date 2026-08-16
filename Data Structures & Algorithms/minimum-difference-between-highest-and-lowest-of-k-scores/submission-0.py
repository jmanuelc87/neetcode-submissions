class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        l, r, n = 0, k - 1, len(nums)
        res = float("inf")

        while r < n:
            d = sorted_nums[r] - sorted_nums[l]
            res = min(res, d)
            l += 1
            r += 1
        
        return res
            