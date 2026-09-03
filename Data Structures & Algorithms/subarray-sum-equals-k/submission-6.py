class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total, res = 0, 0
        prefixSum = {0:1}

        for i in range(len(nums)):
            total += nums[i]
            diff = total - k

            if diff in prefixSum:
                res += prefixSum[diff]
            
            prefixSum[total] = prefixSum.get(total, 0) + 1

        return res
