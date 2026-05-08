MAXN = 10**6
prime = [1] * (MAXN + 1)
prime[0] = prime[1] = 0
for i in range(2, isqrt(MAXN) + 1):
    if prime[i]:
        for j in range(i * i, MAXN + 1, i):
            prime[j] = 0


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        idx = {}
        for k, v in enumerate(nums):
            if k == 0:
                continue
            if v not in idx:
                idx[v] = [k]
            else:
                idx[v].append(k)

        ma = max(nums)
        q = deque()
        q.append(0)
        n = len(nums)
        dist = [-1] * n
        dist[0] = 0
        s = set()
        while q:
            i = q.popleft()
            if i - 1 > 0 and dist[i - 1] == -1:
                dist[i - 1] = dist[i] + 1
                q.append(i - 1)
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = dist[i] + 1
                q.append(i + 1)
            if prime[nums[i]] and nums[i] not in s:
                s.add(nums[i])
                for j in range(nums[i], ma + 1, nums[i]):
                    if j in idx:
                        for k in idx[j]:
                            if dist[k] == -1:
                                dist[k] = dist[i] + 1
                                q.append(k)

        return dist[n - 1]
