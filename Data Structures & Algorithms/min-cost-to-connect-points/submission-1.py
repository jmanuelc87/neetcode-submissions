class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        res = 0
        seen = set()
        heap = [(0, 0)] # initial cost, initial node

        while len(seen) < n:
            cost, node = heapq.heappop(heap)
            
            if node in seen:
                continue
            
            res += cost
            seen.add(node)
            x1, y1 = points[node]

            for nei, (x2, y2) in enumerate(points):
                if nei not in seen and node != nei:
                    n_cost = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heap, (n_cost, nei))

        return res