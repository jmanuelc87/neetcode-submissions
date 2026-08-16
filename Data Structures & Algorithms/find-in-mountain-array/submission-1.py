class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l, r = 1, length - 2
        while l <= r:
            mid = (l+r) // 2
            l, m, r = get(mid - 1), get(mid), get(mid + 1)
            if l < m < r:
                l = mid + 1
            elif l > m > r:
                r = mid - 1
            else:
                break
        peek = mid


        def search(l, r, ascending=True):
            while l <= r:
                m = (l + r) // 2
                t = get(m)
                if t == target:
                    return m
                if ascending == (t < target):
                    l = m + 1
                else:
                    r = m - 1
            return -1

        res = search(0, peek)
        if res != -1:
            return res
        
        return search(peek, length - 1, False)

