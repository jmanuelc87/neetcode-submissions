class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1

        for i, j in counter.items():
            if i == j:
                res = max(res, i)

        return res
