class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suma = [0 for _ in range(len(arr))]
        suma[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            m = max(arr[i+1:])
            suma[i] = m

        return suma