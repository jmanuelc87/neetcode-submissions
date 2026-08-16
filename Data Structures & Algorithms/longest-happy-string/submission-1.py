class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        heap = []

        for ch, n in [("a", a), ("b", b), ("c", c)]:
            if n != 0:
                heapq.heappush(heap, (-n, ch))


        while heap:
            co, ch = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                co2, ch2 = heapq.heappop(heap)
                res += ch2
                co2 += 1
                if co2:
                    heapq.heappush(heap, (co2, ch2))

                heapq.heappush(heap, (co, ch))

            else:
                res += ch
                co += 1

                if co:
                    heapq.heappush(heap, (co, ch))


        return res