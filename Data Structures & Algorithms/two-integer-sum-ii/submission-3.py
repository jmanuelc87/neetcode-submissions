class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        refMap = defaultdict(int)

        for i in range(len(numbers)):
            a = target - numbers[i]
            if refMap[a]:
                return [refMap[a], i + 1]
            refMap[numbers[i]] = i + 1

        return []