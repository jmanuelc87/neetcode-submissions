class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        haystack = self.storage[key]

        l, r = 0, len(haystack) - 1
        res = haystack[0]

        while l <= r:
            m = l + (r - l) // 2
            if haystack[m][1] == timestamp:
                res = haystack[m]
            
            if haystack[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return res[0]
