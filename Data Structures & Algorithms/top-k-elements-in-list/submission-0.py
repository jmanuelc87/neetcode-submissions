from sortedcontainers import SortedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = SortedDict()
        res = []

        for n in nums:
            freq.update({n: freq.get(n, 0) + 1})

        for i in range(k, 0, -1):
            res.append(freq.peekitem(-i)[0])
        
        return res