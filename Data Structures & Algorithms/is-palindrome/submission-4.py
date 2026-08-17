class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p = ""
        for a in s:
            if a.isalnum() and not a.isspace():
                p += a.lower()

        if len(p) == 1:
            return False
        
        for i in range(len(p)//2):
            if p[i] != p[len(p) - i - 1]:
                return False
        return True