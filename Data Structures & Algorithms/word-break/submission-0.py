class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if w == s[i:i+len(w)]:
                    result = dfs(i+len(w))

                    return result
            
            return False
    

        return dfs(0)