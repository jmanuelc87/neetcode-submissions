class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = {}

        def dfs(i):
            # base case, whenever it reaches end of array
            if i == n - 1:
                return True

            if i in cache:
                return cache[i]

            # if we encounter a zero immediately return False, we can't walk any further
            if nums[i] == 0:
                return False

            # calculate the next/end position based on the current jump
            end = min(n, i + nums[i] + 1)

            # iterate valid jump positions
            for j in range(i + 1, end):
                # recursively call next valid jump
                if dfs(j):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        # start at index zero
        return dfs(0)
