class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        shortest = {}
        min_heap = [(0, src)]

        while min_heap:
            wi, srci = heapq.heappop(min_heap)

            if srci in shortest:
                continue
            
            shortest[srci] = wi

            for vj, wj in adj[srci]:
                if vj not in shortest:
                    heapq.heappush(min_heap, [wi + wj, vj])
        


        return shortest