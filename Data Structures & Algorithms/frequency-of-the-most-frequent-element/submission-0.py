class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        l, total, res = 0, 0, 0

        for r in range(len(nums)):
            total += nums_sorted[r]

            while nums_sorted[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res