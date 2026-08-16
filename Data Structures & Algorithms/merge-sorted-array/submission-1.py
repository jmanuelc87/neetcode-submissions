class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1) - 1

        m = m - 1
        n = n - 1
        
        while m >= 0 or n >= 0:
            print(m, n)
            if m >= 0 and n >= 0 and nums1[m] >= nums2[n]:
                nums1[p] = nums1[m]
                nums1[m] = 0
                m -= 1
            elif n >= 0:
                nums1[p] = nums2[n]
                n -= 1
            else:
                break
            
            p -= 1