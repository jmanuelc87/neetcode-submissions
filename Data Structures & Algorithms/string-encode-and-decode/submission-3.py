class Solution:

    def encode(self, strs: List[str]) -> str:
        to = ""
        if len(strs) > 0:
            for l in range(len(strs)):
                if len(strs) - 1 == l:
                    to += strs[l]
                else:
                    to += strs[l] + "\t"
        else:
            return None
        return to

    def decode(self, s: str) -> List[str]:
        to = []
        if s is not None:
            for item in s.split("\t"):
                to.append(item)
        return to