class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgesMap = {i: [] for i in range(n)}
        for a, b in edges:
            edgesMap[a].append(b)
            edgesMap[b].append(a)

        print(edgesMap)

        visited = set()

        def dfs(edge, par):
            if edge in visited:
                return False

            visited.add(edge)
            for e in edgesMap[edge]:
                if e == par:
                    continue
                if not dfs(e, edge):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n