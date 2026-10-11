class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for (ui, vi, ti) in times:
            adj[ui].append((vi, ti))

        minHeap = [(k,0)]
        visited = set()
        t = 0

        while minHeap:
            v1, t1 = heapq.heappop(minHeap)

            if v1 in visited:
                continue

            visited.add(v1)
            t = t1

            for v2, t2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (v2, t1 + t2))

        return t if len(visited) == n else -1