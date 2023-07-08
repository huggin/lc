from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        a = []
        n = len(weights)
        for i in range(1, n):
            a.append(weights[i - 1] + weights[i])

        a.sort()
        return sum(a[n - k : n - 1]) - sum(a[0 : k - 1])
