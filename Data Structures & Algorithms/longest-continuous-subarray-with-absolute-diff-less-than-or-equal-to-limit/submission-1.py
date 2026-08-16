from sortedcontainers import SortedDict

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        diff = SortedDict()
        l = res = 0

        for r, x in enumerate(nums):
            diff[x] = diff.get(x, 0) + 1

            while diff.peekitem(-1)[0] - diff.peekitem(0)[0] > limit:
                y = nums[l]
                diff[y] -= 1
                if diff[y] == 0:
                    del diff[y]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res