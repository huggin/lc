class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        pq = []
        ans = 0
        for s, e, v in events:
            heappush(pq, (-v, -e))
            ans = max(ans, v)
        
        events.sort(key = lambda x : (-x[0], x[1]))
        for s, e, v in events:
            while len(pq) > 0 and -pq[0][1] >= s:
                heappop(pq)
            if len(pq) > 0:
                ans = max(ans, -pq[0][0] + v)
        return ans
