class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        cnt = [1] * n
        
        def union(u, v):
            if cnt[u] < cnt[v]:
                parent[u] = v
                cnt[v] += cnt[u]
            else:
                parent[v] = u
                cnt[u] += cnt[v]
        
        def id(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        for u, v in allowedSwaps:
            u = id(u)
            v = id(v)
            if u != v:
                union(u, v)

        ans = 0
        group = {}
        for i in range(n):
            u = id(i)
            if u not in group:
                group[u] = Counter()
            group[u][source[i]] += 1
        
        for i in range(n):
            u = id(i)
            if target[i] not in group[u] or group[u][target[i]] == 0:
                ans += 1
            else:
                group[u][target[i]] -= 1
        
        return ans
