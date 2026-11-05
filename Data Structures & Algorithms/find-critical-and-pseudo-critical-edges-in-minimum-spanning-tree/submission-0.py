class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)

        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, idx))
            adj[v].append((u, w, idx))
        
        def minmax(src, dst, exclude_idx):
            dist = [float("inf")] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                max_w, u = heapq.heappop(pq)
                if dst == u:
                    return max_w
                
                for v, w, eidx in adj[u]:
                    if eidx == exclude_idx:
                        continue
                    new_w = max(max_w, w)
                    if new_w < dist[v]:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w, v))

            return float("inf")

        critical, pseudo = [], []
        for idx, (u, v, w) in enumerate(edges):
            if w < minmax(u, v, idx):
                critical.append(idx)
            elif w == minmax(u, v, -1):
                pseudo.append(idx)

        return [critical, pseudo]