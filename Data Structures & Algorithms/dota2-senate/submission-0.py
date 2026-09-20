class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "D":
                D.append(i)
            else:
                R.append(i)

        
        while D and R:
            dt = D.popleft()
            rt = R.popleft()

            if dt < rt:
                D.append(rt + n)
            else:
                R.append(dt + n)

        return "Radiant" if R else "Dire"