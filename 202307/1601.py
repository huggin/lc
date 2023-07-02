from typing import List


class Solution:
    def countBit(self, n):
        ans = 0
        while n:
            ans += 1
            n &= n - 1
        return ans

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        ans = 0
        for i in range(1, 1 << m):
            house = n * [0]
            for j in range(m):
                if i & (1 << j):
                    house[requests[j][0]] -= 1
                    house[requests[j][1]] += 1

            if max(house) == 0:
                ans = max(ans, self.countBit(i))

        return ans
