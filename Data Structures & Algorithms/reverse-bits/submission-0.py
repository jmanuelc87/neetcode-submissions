class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        while n:
            t = (n & 0x1)
            n = n >> 1
            r = (t & 0x1) << 1