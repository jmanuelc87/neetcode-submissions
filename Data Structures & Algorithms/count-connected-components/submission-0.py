class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for source, sink in edges:
            adjMap[source].append(sink)
            adjMap[sink].append(source)
        
        visited = set()

        def dfs(node):
            for nei in adjMap[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        total = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                total += 1
        
        return total