class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = []
        for passenger in details:
            age = passenger[11:13]
            res.append(int(age))
        
        counter = Counter(res)
        older = 0
        for k, v in counter.items():
            if k > 60:
                older += 1
        return older