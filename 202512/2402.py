class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        unused = []
        for i in range(n):
            heappush(unused, i)
        used = []
        meetings.sort()
        for s, e in meetings:
            while used and used[0][0] <= s:
                _, i = heappop(used)
                heappush(unused, i)
            if len(unused) > 0:
                i = heappop(unused)
                rooms[i] += 1
                heappush(used, (e, i))
            else:
                time, i = heappop(used)
                rooms[i] += 1
                heappush(used, (time + e - s, i))

        return rooms.index(max(rooms))
