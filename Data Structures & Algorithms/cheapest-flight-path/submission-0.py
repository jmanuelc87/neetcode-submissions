class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        heap = [(src, 0, -1)]
        dist = [[float("inf")] * (k + 5) for _ in range(n)]
        for src, dst, price in flights:
            adj[src].append((dst, price))

        dist[src][0] = 0
        while heap:
            sii, cost, stops = heapq.heappop(heap)

            if sii == dst:
                return cost

            if stops == k or dist[sii][stops + 1] < cost:
                continue

            for nii, new_cost in adj[sii]:
                nextCost = cost + new_cost
                nextStop = 1 + stops
                if dist[nii][nextStop + 1] > nextCost:
                    dist[nii][nextStop + 1] = nextCost
                    heapq.heappush(heap, (nii, nextCost, nextStop))

        return -1