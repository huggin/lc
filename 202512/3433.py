class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans = [0] * n
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))
        print(events)
        online = [1] * n
        pq = []
        for m, ts, ids in events:
            while len(pq) > 0 and pq[0][0] <= int(ts):
                curr = heapq.heappop(pq)
                online[curr[1]] = 1
            if m == "OFFLINE":
                online[int(ids)] = 0
                heapq.heappush(pq, (int(ts) + 60, int(ids)))
            elif ids == "ALL":
                for j in range(n):
                    ans[j] += 1
            else:
                if ids == "HERE":
                    for i in range(n):
                        if online[i] == 1:
                            ans[i] += 1
                else:
                    for s in ids.split():
                        ans[int(s[2:])] += 1

        return ans
