class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}

        def dfs(cur):
            if cur < 0:
                return float("inf")
            if cur in [2, 3]:
                return 1
            if cur in cache:
                return cache[num]
            
            ops = min(dfs(cur - 2), dfs(cur - 3))
            cache[num] = ops + 1
            return cache[num]

        freq = Counter(nums)
        res = 0
        for num, cnt in freq.items():
            op = dfs(cnt)
            if op == float("inf"):
                return -1
            res += op
        
        return res