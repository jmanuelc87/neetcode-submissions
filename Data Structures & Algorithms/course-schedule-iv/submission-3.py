class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)

        for pre, course in prerequisites:
            adj[pre].append(course)

        def dfs(course, target):
            if course == target:
                return True
            for pre in adj[course]:
                if dfs(pre, target):
                    return True
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        
        return res