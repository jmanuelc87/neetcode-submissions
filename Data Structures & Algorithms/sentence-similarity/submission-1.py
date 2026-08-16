class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        wtosm = defaultdict(set)

        for s1, s2 in similarPairs:
            wtosm[s1].add(s2)
            wtosm[s2].add(s1)
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wtosm[sentence1[i]]:
                continue
            return False
        
        return True