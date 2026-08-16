class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_sort = sorted(people)
        l, r, a = 0, len(people_sort) - 1, 0

        while l <= r:
            remain = limit - people_sort[r]
            r -= 1
            a += 1

            if l <= r and remain >= people_sort[l]:
                l += 1

        return a