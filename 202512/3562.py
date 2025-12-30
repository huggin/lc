class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u-1].append(v-1)
        
        def dfs(u):
            a = [-inf] * (budget + 1)
            b = [-inf] * (budget + 1)
            a[0] = 0
            b[0] = 0
            for v in g[u]:
                va, vb = dfs(v)
                temp = [-inf] * (budget + 1)
                for i in range(budget + 1):
                    if a[i] >= 0:
                        for j in range(budget - i + 1):
                            if va[j] >= 0:
                                temp[i+j] = max(temp[i+j], a[i] + va[j])
                a = temp
                temp = [-inf] * (budget + 1)
                for i in range(budget + 1):
                    if b[i] >= 0:
                        for j in range(budget - i + 1):
                            if vb[j] >= 0:
                                temp[i+j] = max(temp[i+j], b[i] + vb[j])
                b = temp
            
            ua = a[:]
            ub = a[:]
            c1 = present[u]
            r1 = future[u] - c1
            c2 = present[u] // 2
            r2 = future[u] - c2
            for i in range(c1, budget+1):
                if b[i-c1] >= 0:
                    ua[i] = max(ua[i], b[i-c1] + r1)
            for i in range(c2, budget+1):
                if b[i-c2] >= 0:
                    ub[i] = max(ub[i], b[i-c2] + r2)
            return ua, ub
        
        ua, ub = dfs(0)
        return max(ua)
