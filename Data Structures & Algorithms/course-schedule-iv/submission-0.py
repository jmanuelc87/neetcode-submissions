class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)


        def dfs(node):
            if node not in prereqMap:
                prereqMap[node] = set()
                for pre in adj[node]:
                    prereqMap[node] |= dfs(pre)
                prereqMap[node].add(node)
            return prereqMap[node]

        prereqMap = {}
        for node in range(numCourses):
            dfs(node)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res