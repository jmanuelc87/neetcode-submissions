class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        cache = {}

        for i in range(n):
            cache[target - nums[i]] = i
 
        for i in range(n):
            if nums[i] in cache:
                t1 = cache[nums[i]]
                if nums[i] != nums[t1] and nums[i] + nums[t1] == target:
                    return [i, t1]
        
        return [0, 0]