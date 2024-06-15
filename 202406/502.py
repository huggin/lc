class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        a = []
        n = len(profits)
        for i in range(n):
            a.append((profits[i], capital[i]))

        a.sort(key=lambda x: x[1])
        pq = []
        for b in a:
            while k > 0 and b[1] > w and len(pq) > 0:
                k -= 1
                w += -heapq.heappop(pq)
            if b[1] <= w:
                heapq.heappush(pq, -b[0])

        while k > 0 and len(pq) > 0:
            k -= 1
            w += -heapq.heappop(pq)
        return w
