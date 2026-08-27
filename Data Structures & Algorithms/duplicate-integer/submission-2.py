class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for k, el in count.items():
            if el > 1:
                return True
        
        return False