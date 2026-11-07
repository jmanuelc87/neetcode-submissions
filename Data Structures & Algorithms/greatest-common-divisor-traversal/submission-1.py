class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.n -= 1

        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.size[pu] += self.size[pv]
        self.parent[pv] = pu

        return True

    def isConnected(self):
        return self.n == 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        fi = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in fi:
                        uf.union(i, fi[f])
                    else:
                        fi[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in fi:
                    uf.union(i, fi[n])
                else:
                    fi[n] = i

        return uf.isConnected()
