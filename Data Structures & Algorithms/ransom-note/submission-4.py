class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        for c in c1:
            if c2[c] < c1[c]:
                return False
        
        return True