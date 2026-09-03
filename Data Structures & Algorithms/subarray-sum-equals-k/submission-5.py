class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total, res = 0, 0
        prefixSum = {0: 1}

        for i in range(n):
            total += nums[i]
            diff = total - k

            if diff in prefixSum:
                res += prefixSum[diff]
            
            if total not in prefixSum:
                prefixSum[total] = 1
            else:
                prefixSum[total] += 1

        return res
