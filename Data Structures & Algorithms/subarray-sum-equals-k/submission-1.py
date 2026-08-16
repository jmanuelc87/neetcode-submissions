class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        total_sum = 0
        res = 0

        for i in range(0, len(nums)):
            total_sum += nums[i]
            diff = total_sum - k

            if diff in prefixSum:
                res += prefixSum[diff]

            if total_sum not in prefixSum:
                prefixSum[total_sum] = 1
            else:
                prefixSum[total_sum] += 1         

        return res
            