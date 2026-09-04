class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax, gmin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0

        for num in nums:
            curmax = max(curmax + num, num)
            curmin = min(curmin + num, num)

            total += num

            gmax = max(gmax, curmax)
            gmin = min(gmin, curmin)

        
        return max(gmax, total - gmin) if gmax > 0 else gmax