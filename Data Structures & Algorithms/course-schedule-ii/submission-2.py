class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output


