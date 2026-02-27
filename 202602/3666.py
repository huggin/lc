class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n, z = len(s), s.count("0")
        dist = [-1] * (n + 1)
        v = [SortedList(range(0, n + 1, 2)), SortedList(range(1, n + 1, 2))]
        q = deque([z])
        dist[z] = 0
        v[z % 2].remove(z)
        while q:
            z = q.popleft()
            c1, c2 = max(0, k - n + z), min(k, z)
            zl, zr = z + k - 2 * c2, z + k - 2 * c1
            idx = v[zl % 2].bisect_left(zl)
            while idx < len(v[zl % 2]) and v[zl % 2][idx] <= zr:
                z2 = v[zl % 2][idx]
                dist[z2] = dist[z] + 1
                q.append(z2)
                v[zl % 2].pop(idx)

        return dist[0]
