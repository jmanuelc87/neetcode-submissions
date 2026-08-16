class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)

        for x in ransomNote:
            if x not in magazine:
                return False
            else:
                magazine.remove(x)
        
        return True
