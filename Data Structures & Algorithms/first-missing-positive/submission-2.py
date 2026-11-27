class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m = 1

        for n in nums:
            if n > 0 and n == m:
                m += 1
        
        return m