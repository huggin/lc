from sortedcontainers import SortedList


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        d = SortedList(hand)

        for i in range(n // groupSize):
            curr = d[0]
            d.pop(0)
            for j in range(1, groupSize):
                curr += 1
                k = d.bisect_left(curr)
                if k == len(d) or d[k] != curr:
                    return False
                d.pop(k)
        return True
