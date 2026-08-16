class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            k = (l + r) // 2
            sq = k * k
            
            if sq > num:
                r = k - 1
            elif sq < num:
                l = k + 1
            else:
                return True
        
        return False
