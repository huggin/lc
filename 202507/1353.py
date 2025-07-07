class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        ans = 0
        pq = []
        n = len(events)
        i = 0
        while i < n:
            if len(pq) == 0:
                curr = events[i][0]
            while i < n and events[i][0] <= curr:
                heappush(pq, events[i][1])
                i += 1
            if len(pq) > 0:
                t = heappop(pq)
                if t >= curr:
                    ans += 1
                    curr += 1
        while len(pq) > 0:
            t = heappop(pq)
            if t >= curr:
                ans += 1
                curr += 1
        return ans
