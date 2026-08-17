class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        res = len(ransomNote)
        for a, b in zip(ransomCounter.items(), magazineCounter.items()):
            if b[1] == a[1]:
                res -= a[1]

        return res == 0