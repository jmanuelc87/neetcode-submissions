class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for n in nums:
            i = abs(n) - 1

            if i >= 0 and i < len(nums) and nums[i] > 0:
                nums[i] *= -1
            elif i >= 0 and i < len(nums) and nums[i] == 0:
                nums[i] = -(len(nums) + 1)

        # print(nums)

        for k in range(1, len(nums) + 1):
            i = k - 1
            # print(i)
            if i >= 0 and i < len(nums) and nums[i] >= 0:
                return k
        
        return len(nums) + 1