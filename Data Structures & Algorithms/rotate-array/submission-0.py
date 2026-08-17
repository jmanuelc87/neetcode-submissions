class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for _ in range(k):
            tmp = nums[n-1]
            for j in range(n-1, -1, - 1):
                nums[j] = nums[j - 1]
                # print(nums)
            nums[0] = tmp
