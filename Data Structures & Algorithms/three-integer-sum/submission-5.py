class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for j in range(len(nums)):
            if nums[j] > 0:
                break

            if j > 0 and nums[j] == nums[j - 1]:
                continue

            l, r = j + 1, len(nums) - 1
            while l < r:
                cur = nums[j] + nums[l] + nums[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    


        return res