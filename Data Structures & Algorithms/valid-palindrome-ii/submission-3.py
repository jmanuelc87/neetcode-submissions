class Solution:
    def validPalindrome(self, s: str) -> bool:

        if len(s) <= 2:
            return True

        n = len(s)
        count = 0
        l, r = 0, n - 1

        for pos in range(n):
            print(s[0:pos] + s[pos+1:n])
            while l < r:
                print(count, l, r, (pos != l or pos != r), s[l] == s[r])
                if (pos != l or pos != r) and s[l] == s[r]:
                    count += 1
                l += 1
                r -= 1

            print(count, n//2)
            if count == n // 2:
                return True
            
            l = 0
            r = n - 1
            count = 0
        
        return False