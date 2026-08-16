class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)

        for pre, course in prerequisites:
            adj[course].append(pre)

        prereqMap = defaultdict(set)
        def dfs(course):
            if course not in prereqMap:
                for pre in adj[course]:
                    prereqMap[course] |= dfs(pre)
                prereqMap[course].add(course)
            return prereqMap[course]

        for course in range(numCourses):
            dfs(course)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])

        return res
