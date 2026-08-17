class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[p].append(c)

        visited = set()
        path = set()

        def dfs(course, ordering):
            if course in visited:
                return False
            
            if len(preMap[course]) == 0:
                ordering.add(course)
                return True
            
            visited.add(course)

            for crs in preMap[course]:
                if not dfs(crs, ordering):
                    return False

            ordering.add(course)

            visited.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, path):
                return []
        
        return list(path)


