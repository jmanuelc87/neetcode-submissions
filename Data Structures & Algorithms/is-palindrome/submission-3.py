class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p = ""
        for a in s:
            if a.isalpha() and not a.isspace():
                p += a.lower()

        for i in range(len(p)//2):
            if p[i] != p[len(p) - i - 1]:
                return False
        return True