class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, ns in enumerate(nums):
            cache[ns] = i
 
        for i, ns in enumerate(nums):
            diff = target - ns
            if diff in cache and cache[diff] != i:
                return [i, cache[diff]]
        
        return []