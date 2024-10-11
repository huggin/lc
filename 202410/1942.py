from sortedcontainers import SortedList


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends = []
        for k, v in enumerate(times):
            friends.append((v[0], 1, k))
            friends.append((v[1], 0, k))

        heapq.heapify(friends)
        used = SortedList()
        d = {}

        while len(friends) > 0:
            f = heapq.heappop(friends)
            if f[1] == 1:
                if len(used) == 0:
                    used.add((0, 1))
                    d[f[2]] = (0, 1)
                    ans = 0
                elif used[0][0] != 0:
                    ans = 0
                    d[f[2]] = (0, 1)
                    if used[0][0] == 1:
                        curr = used.pop(0)
                        used.add((0, curr[1]))
                    else:
                        used.add((0, 1))
                else:
                    curr = used[0]
                    ans = curr[1]
                    d[f[2]] = (curr[1], curr[1] + 1)
                    if len(used) > 1 and used[1][0] - used[0][1] == 1:
                        curr = (used[0][0], used[1][1])
                        used.pop(1)
                        used.pop(0)
                        used.add(curr)
                    else:
                        used.pop(0)
                        used.add((curr[0], curr[1] + 1))
                if f[2] == targetFriend:
                    return ans
            else:
                j = used.bisect(d[f[2]])
                if j == len(used) or used[j][0] > d[f[2]][0]:
                    j -= 1
                curr = used.pop(j)
                if curr[0] != d[f[2]][0]:
                    used.add((curr[0], d[f[2]][0]))
                if d[f[2]][0] + 1 != curr[1]:
                    used.add((d[f[2]][0] + 1, curr[1]))
        return -1
