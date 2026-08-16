class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for si, ti in zip(s, t):
            if si != ti:
                return False
        
        return True