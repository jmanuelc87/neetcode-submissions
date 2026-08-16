class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0

        for num, cnt in freq.items():
            if cnt == 1:
                return -1
            res += math.ceil(cnt / 3)
        
        return res