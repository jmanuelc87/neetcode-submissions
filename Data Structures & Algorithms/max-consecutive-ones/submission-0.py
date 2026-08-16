class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, curr = 0, 0

        for i in range(len(nums)):
            if 1 == nums[i]:
                curr += 1
            else:
                curr = 0

            maxCount = max(maxCount, curr)

        return maxCount 