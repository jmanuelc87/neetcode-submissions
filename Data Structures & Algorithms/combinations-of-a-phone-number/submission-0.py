class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, current):
            if len(current) == len(digits) and len(current) > 0:
                res.append("".join(current))
                return

            for k in range(3):
                if i < len(digits):
                    current.append(map[digits[i]][k])
                    dfs(i + 1, current)
                    current.pop()

        dfs(0, [])

        return res