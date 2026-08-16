class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r, l = 0, n - 1
        result = [0] * n

        for num in nums:
            if num % 2 == 0:
                result[r] = num
                r += 1
            else:
                result[l] = num
                l -= 1

        return result