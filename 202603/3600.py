class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def merge(u, v):
            if size[u] < size[v]:
                parent[u] = v
                size[v] += size[u]
            else:
                parent[v] = u
                size[u] += size[v]

        edges.sort(key=lambda x: (-x[3], -x[2]))
        ans = 10**6
        cnt = 0

        for u, v, w, must in edges:
            ui = find(u)
            vi = find(v)
            if must:
                ans = min(ans, w)
                if ui == vi:
                    return -1
                merge(ui, vi)
                cnt += 1
            else:
                if ui == vi:
                    continue
                merge(ui, vi)
                if n - 1 - cnt <= k:
                    ans = min(ans, w * 2)
                    k -= 1
                else:
                    ans = min(ans, w)
                cnt += 1
        return ans if cnt == n - 1 else -1
