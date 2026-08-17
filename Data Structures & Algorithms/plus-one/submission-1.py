class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        remainder = 0
        increment = 1

        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                remainder = 1
            elif 0 <= digits[i] < 9:
                digits[i] += increment
                increment = 0
                remainder = 0

        if remainder:
            digits.insert(0, 1)

        return digits