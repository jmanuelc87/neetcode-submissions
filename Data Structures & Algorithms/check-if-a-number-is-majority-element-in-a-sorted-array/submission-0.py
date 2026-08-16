class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        fi = self.lower_bound(nums, target)
        return fi + len(nums) // 2 < len(nums) and nums[fi + len(nums) // 2] == target

    def lower_bound(self, nums, target):
        s = 0
        e = len(nums) - 1
        i = len(nums)

        while s <= e:
            m = (s + e) // 2
            if nums[m] >= target:
                e = m - 1
                i = m
            else:
                s = m + 1
        
        return i