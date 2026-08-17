class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return True


        count = 0
        l, r = 0, n - 1

        for pos in range(n - 1):
            while l <= r:
                if (pos != l or pos != r) and s[l] == s[r]:
                    count += 1
                l += 1
                r -= 1

            if count == (n // 2):
                return True
            
            l = 0
            r = n - 1
            count = 0
        
        return False