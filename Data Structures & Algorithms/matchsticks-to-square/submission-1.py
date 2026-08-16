class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        if n % 4 != 0:
            return False

        l = n // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for k in range(4):
                if sides[k] + matchsticks[i] <= l:
                    sides[k] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[k] -= matchsticks[i]
                
                if sides[k] == 0:
                    break
            
            return False
        
        return dfs(0)