class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res, n = set(), len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                l, r = j+1, n-1

                while l < r:
                    curr_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[l] + sorted_nums[r]

                    if curr_sum == target:
                        res.add(
                            (sorted_nums[i], sorted_nums[j], sorted_nums[l], sorted_nums[r])
                        )
                        l, r = l + 1, r - 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
        

        return [list(t) for t in res]