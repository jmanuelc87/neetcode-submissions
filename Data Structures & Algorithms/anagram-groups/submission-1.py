class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for a in strs:
            k = "".join(sorted(a))
            grouped[k].append(a)

        
        return list(grouped.values())