class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r,res=1,n,0

        while l <= r:
            k = (l + r) // 2
            coins = (k/2) * (k+1)

            if coins > n:
                r = k - 1
            else:
                l = k + 1
                res = max(res, k)
        
        return res
