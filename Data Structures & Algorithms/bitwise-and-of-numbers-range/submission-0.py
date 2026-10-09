class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left

        for j in range(left + 1, right + 1):
            res &= j
        
        return res
