class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)

        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)
        
        def dfs(n, p):
            time = 0

            for ci in adj[n]:
                if ci == p:
                    continue
                childTime = dfs(ci, n)
                if childTime > 0 or hasApple[ci]:
                    time += 2 + childTime
            return time
        
        return dfs(0, -1)
