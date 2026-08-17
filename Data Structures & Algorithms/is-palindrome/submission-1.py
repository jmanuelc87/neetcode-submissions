class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        count = 0

        s = re.sub('[^a-z]', '', s.lower())
        half = len(s) // 2
        size = len(s) - 1

        if size % 2 == 0 and s[half] == s[size]:
            count += 1

        for i in range(half):
            if s[i] == s[size - i]:
                count += 1

        return half == count