class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, numZeroes, longest = 0, 0, 0, 0

        while r < len(nums):
            if nums[r] == 0:
                numZeroes += 1
            
            while numZeroes == 2:
                if nums[l] == 0:
                    numZeroes -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

            r += 1
        
        return longest