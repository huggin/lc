class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, a in enumerate(arr):
            d[a].append(i)

        n = len(arr)
        v = [-1] * n
        q = deque()
        q.append(0)
        v[0] = 0
        v2 = set()
        while q:
            i = q.popleft()
            if i - 1 >= 0 and v[i - 1] == -1:
                v[i - 1] = v[i] + 1
                q.append(i - 1)
            if i + 1 < n and v[i + 1] == -1:
                v[i + 1] = v[i] + 1
                q.append(i + 1)
            if arr[i] not in v2:
                v2.add(arr[i])
                for j in d[arr[i]]:
                    if v[j] == -1:
                        v[j] = v[i] + 1
                        q.append(j)
        return v[-1]
