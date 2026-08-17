class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)

        edge_cnt = {}
        leves = deque()
        for src, nei in adj.items():
            if len(nei) == 1:
                leves.append(src)
            edge_cnt[src] = len(nei)


        while leves:
            if n <= 2:
                return list(leves)
            for i in range(len(leves)):
                node = leves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leves.append(nei)