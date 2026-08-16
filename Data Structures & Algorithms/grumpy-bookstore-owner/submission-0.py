class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        window = 0
        maxWindow = 0

        l, r = 0, minutes

        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1

            maxWindow = max(maxWindow, window)
        
        return satisfied + maxWindow