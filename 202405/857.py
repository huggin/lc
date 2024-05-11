import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        emp = []
        for i in range(n):
            emp.append((wage[i] / quality[i], quality[i]))

        emp.sort(key=lambda x: (x[0], x[1]))
        cnt = 0
        pq = []

        for i in range(k):
            cnt += emp[i][1]
            heapq.heappush(pq, -emp[i][1])
        ans = emp[k - 1][0] * cnt

        for i in range(k, n):
            cnt = cnt + pq[0] + emp[i][1]
            ans = min(ans, emp[i][0] * cnt)
            heapq.heapreplace(pq, -emp[i][1])

        return ans
