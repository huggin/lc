class Solution:
    def maxDifference(self, s: str) -> int:
        C = Counter(s)
        a, b = -1, -1
        for _, v in C.most_common():
            if v % 2 == 1:
                if a == -1:
                    a = v
            else:
                b = v
        return a - b
