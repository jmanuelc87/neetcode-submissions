class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = "0"

        for i in range(2, len(num)):
            if num[i] == num[i - 1] and num[i - 1] == num[i - 2]:
                a = num[i] + num[i - 1] + num[i - 2]
                res = max(res, a)

        return "" if res == "0" else res