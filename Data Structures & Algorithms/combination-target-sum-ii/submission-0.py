class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        freq = defaultdict(int)
        res, current = [], []

        def backtrack(i, nums, current, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if target < 0 or i >= len(nums):
                return

            if freq[nums[i]] > 0:
                current.append(nums[i])
                freq[nums[i]] -= 1
                backtrack(i, nums, current, target - nums[i])
                freq[nums[i]] += 1
                current.pop()
            
            backtrack(i + 1, nums, current, target)

        for c in candidates:
            freq[c] += 1

        backtrack(0, list(freq.keys()), current, target)

        return res

