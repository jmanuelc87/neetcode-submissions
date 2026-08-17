class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        count = 0

        s = re.sub('[^a-z]', '', s.lower())
        half = len(s) // 2
        size = len(s) - 1

        print(s)
        for i in range(half):
            print(i, size-i)
            if s[i] == s[size - i]:
                count += 1
                print('.')

        return half == count