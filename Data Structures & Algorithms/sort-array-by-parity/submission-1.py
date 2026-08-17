class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, 0, n // 2
        result = [0] * n

        while i < n // 2 and k < n:
            j = i
            while j < n:
                if j < n and nums[j] % 2 == 0:
                    result[i] = nums[j]
                    i += 1
                elif k < n:
                    result[k] = nums[j]
                    k += 1
                j += 1

        return result