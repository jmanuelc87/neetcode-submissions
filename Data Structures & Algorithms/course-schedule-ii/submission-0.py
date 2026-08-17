class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[p].append(c)

        visited = set()
        path = []

        def dfs(course, ordering):
            if course in visited:
                return False
            
            if len(preMap[course]) == 0:
                ordering.append(course)
                return True
            
            visited.add(course)
            ordering.append(course)

            for crs in preMap[course]:
                if not dfs(crs, ordering):
                    return False

            ordering.append(course)

            visited.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, path):
                return []
        
        return path


