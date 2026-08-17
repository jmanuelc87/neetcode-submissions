class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def dfs(cur):
            if cur < 0:
                return float("inf")
            if cur == 0:
                return 0
            
            ops = min(dfs(cur - 2), dfs(cur - 3))
            return 1 + ops

        freq = Counter(nums)
        res = 0
        for num, cnt in freq.items():
            op = dfs(cnt)
            if op == float("inf"):
                return -1
            res += op
        
        return res