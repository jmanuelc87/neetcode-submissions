class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        n = len(rectangles)
        ratios = []
        for i in range(n):
            w, h = rectangles[i]
            ratios.append(w/h)
        counter = Counter(ratios)
        res = 0
        for v in counter.values():
            if v > 1:
                res += (v * (v - 1)) // 2
        
        return res