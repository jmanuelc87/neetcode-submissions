class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if i+len(w) <= len(s) and w == s[i:i+len(w)]:
                    if dfs(i + len(w)):
                        return True
            
            return False
    

        return dfs(0)