class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize:
            return False

        hand.sort()
        freq = Counter(hand)

        for i in hand:
            if freq[i]:
                for j in range(i, min(i + groupSize, n)):
                    if not freq[j]:
                        return False

                    freq[j] -= 1

        return True
