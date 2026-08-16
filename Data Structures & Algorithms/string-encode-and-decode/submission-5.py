class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        res = f"{len(strs)}|"
        for s in strs:
            res += f"{len(s)}#{s},"

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        le, i = "", 0

        while s[i] != "|":
            le += s[i]
            i += 1

        for _ in range(int(le)):
            la = ""
            while s[i] != "#":
                la += s[i]
                i += 1

            lb = ""
            for _ in range(int(la[1:]) + 1):
                lb += s[i]
                i += 1

            res.append(lb[1:])

        return res