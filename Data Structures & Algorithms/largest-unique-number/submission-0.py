class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = -1

        for n in nums:
            freq[n] += 1
        
        for k, v in freq.items():
            if v == 1:
                res = max(res, k)
    
        return res