class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        for  k, (s1, s2) in enumerate(zip(sentence1, sentence2)):
            if similarPairs and s1 not in similarPairs[k] and s2 not in similarPairs[k]:
                return False
        
        return True