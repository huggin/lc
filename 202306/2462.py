import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = 0, len(costs) - 1
        pq1 = []
        pq2 = []

        (
            lc,
            rc,
        ) = (
            0,
            0,
        )
        while i <= j:
            if lc < candidates:
                heapq.heappush(pq1, costs[i])
                i += 1
                lc += 1
            elif rc < candidates:
                heapq.heappush(pq2, costs[j])
                j -= 1
                rc += 1
            else:
                break

        ans = 0
        for _ in range(k):
            if len(pq2) == 0 or len(pq1) > 0 and pq1[0] <= pq2[0]:
                ans += pq1[0]
                if i <= j:
                    heapq.heapreplace(pq1, costs[i])
                    i += 1
                else:
                    heapq.heappop(pq1)
            else:
                ans += pq2[0]
                if i <= j:
                    heapq.heapreplace(pq2, costs[j])
                    j -= 1
                else:
                    heapq.heappop(pq2)

        return ans
