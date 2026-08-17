class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1) - 1
        
        while m > 0 or n > 0:
            if m - 1 >= 0 and n - 1 >= 0 and nums1[m - 1] >= nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                nums1[m - 1] = 0
                m -= 1
            else:
                if n - 1 >= 0:
                    nums1[p] = nums2[n - 1]
                    n -= 1
            
            p -= 1