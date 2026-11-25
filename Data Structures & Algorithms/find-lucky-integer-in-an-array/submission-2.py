class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        a = -1
        for k, v in counter.items():
            if k == v:
                a = max(a, k)

        return a