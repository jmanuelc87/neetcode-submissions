class Solution:
    def confusingNumber(self, n: int) -> bool:
        num = f"{n}"
        inverted = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        rotated_number = []

        for c in num:
            if c in [2, 3, 4, 5, 7]:
                return False
            rotated_number.append(inverted[c])

        rotated_number = "".join(rotated_number)

        return int(rotated_number[::-1]) != n