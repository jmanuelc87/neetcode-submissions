class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        T = {}
        for c in t:
            T[c] = 1 + T.get(c, 0)
        
        res, L = [-1, 1], float("infinity")
        for i in range(len(s)):
            cS = {}
            for j in range(i, len(s)):
                cS[s[j]] = 1 + cS.get(s[j], 0)

                flag = True
                for c in T:
                    if T[c] > cS.get(c, 0):
                        flag = False
                        break
                
                if flag and (j - i + 1) < L:
                    L = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if L != float("infinity") else ""
