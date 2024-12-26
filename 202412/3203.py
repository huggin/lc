class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def longestPath(tree):
            n = len(tree) + 1
            g = [[] for _ in range(n)]
            for i, j in tree:
                g[i].append(j)
                g[j].append(i)
            
            v = [-1] * n
            q = deque()
            q.append(0)
            v[0] = 0
            while len(q) > 0:
                u = q.popleft()
                for w in g[u]:
                    if v[w] == -1:
                        v[w] = v[u] + 1
                        q.append(w)
            
            u, d = -1, 0
            for i in range(n):
                if v[i] > d:
                    d = v[i]
                    u = i
            
            q.append(u)
            v = [-1] * n
            v[u] = 0
            while len(q) > 0:
                u = q.popleft()
                for w in g[u]:
                    if v[w] == -1:
                        v[w] = v[u] + 1
                        q.append(w)
        
            return max(v)
        
        d1 = longestPath(edges1)
        d2 = longestPath(edges2)
        
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

    
