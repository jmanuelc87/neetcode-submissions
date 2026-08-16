class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        left_shifts = 0
        for d, a in shift:
            if d == 1:
                a = -a
            left_shifts += a

        left_shifts %= len(s)
        s = s[left_shifts:] + s[:left_shifts]

        return s