from functools import cache
from typing import List


class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        n = len(locations)
        M = int(1e9 + 7)

        @cache
        def f(k, fuel):
            ans = 1 if k == finish else 0

            for i in range(n):
                if i == k:
                    continue
                need = abs(locations[i] - locations[k])
                if need <= fuel:
                    ans = (ans + f(i, fuel - need)) % M

            return ans

        return f(start, fuel)
