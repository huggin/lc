class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        n = len(classes)
        for a, b in classes:
            heapq.heappush(pq, (a / b - (a+1) / (b+1), a, b))

        for _ in range(extraStudents):
            r, a, b = heapq.heappop(pq)
            heapq.heappush(pq, ((a+1) / (b+1) - (a+2)/(b+2), a+1, b+1))
        
        ans = 0
        for _, a, b in pq:
            ans += a / b
        return ans / n
