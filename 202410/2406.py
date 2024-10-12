class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for it in intervals:
            if len(pq) > 0 and pq[0] < it[0]:
                heapq.heapreplace(pq, it[1])
            else:
                heapq.heappush(pq, it[1])

        return len(pq)
