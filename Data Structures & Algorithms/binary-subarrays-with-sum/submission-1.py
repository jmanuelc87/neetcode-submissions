class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum, res = 0, 0

        count = { 0: 1 }

        for n in nums:
            prefixSum += n
            res += count.get(prefixSum - goal, 0)
            count[prefixSum] = count.get(prefixSum, 0) + 1

        return res