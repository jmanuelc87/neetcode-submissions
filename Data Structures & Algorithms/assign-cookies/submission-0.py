class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        happyChildren, p = 0, 0

        for greed in g:
            if s[p] >= greed:
                happyChildren += 1
                p += 1
        

        return happyChildren