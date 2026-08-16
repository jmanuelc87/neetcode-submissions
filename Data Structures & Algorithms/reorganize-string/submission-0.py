class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = []
        while len(res) < len(s):
            midx = freq.index(max(freq))
            c = chr(midx + ord("a"))
            res.append(c)
            freq[midx] -= 1
            if freq[midx] == 0:
                continue

            tmp = freq[midx]
            freq[midx] = float("-inf")
            nmidx = freq.index(max(freq))
            char = chr(nmidx + ord("a"))
            res.append(char)
            freq[midx] = tmp
            freq[nmidx] -= 1
        
        return "".join(res)