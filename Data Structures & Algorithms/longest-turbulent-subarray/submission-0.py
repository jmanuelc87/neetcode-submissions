class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        cache = {}

        def dfs(i, sign):
            if i == n - 1:
                return 1

            if (i, sign) in cache:
                return cache[(i, sign)]

            res = 1
            if (sign and arr[i] > arr[i+1]) or (not sign and arr[i] < arr[i+1]):
                res = 1 + dfs(i+1, not sign)
            
            cache[(i, sign)] = res
            
            return res
        
        maxlen = 1
        for i in range(n):
            maxlen = max(maxlen, dfs(i, True), dfs(i, False))
        
        return maxlen