class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                current.append(nums[j])
                dfs(j, current, total + nums[j])
                current.pop()

        dfs(0, [], 0)
        return result
