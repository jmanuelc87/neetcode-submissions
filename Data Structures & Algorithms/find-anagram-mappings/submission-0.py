class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = {}
        n = len(nums1)

        for j in range(n):
            pos[nums2[j]] = j

        res = [0] * n
        for i in range(n):
            res[i] = pos[nums1[i]]

        return res