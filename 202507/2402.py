class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        pq = []
        cnt = [0] * n
        rooms = list(range(n))
        heapify(rooms)
        for b, e in meetings:
            while pq and pq[0][0] <= b:
                _, r = heappop(pq)
                heappush(rooms, r)
            if rooms:
                j = heappop(rooms)
                cnt[j] += 1
                heappush(pq, (e, j))
            else:
                finish, r = heappop(pq)
                heappush(pq, (e - b + finish, r))
                cnt[r] += 1

        ans = -1
        ma = 0
        for i in range(n):
            if cnt[i] > ma:
                ans = i
                ma = cnt[i]
        return ans
