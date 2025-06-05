class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def id(u):
            while parent[u] != u:
                u = parent[u]
            return u
        
        def merge(u, v):
            if u < v:
                parent[v] = u
            else:
                parent[u] = v
        
        for i in range(len(s1)):
            u = ord(s1[i]) - ord('a')
            v = ord(s2[i]) - ord('a')
            u = id(u)
            v = id(v)
            if u != v:
                merge(u, v)
        
        ans = []
        for c in baseStr:
            u = ord(c) - ord('a')
            ans.append(chr(ord('a') + id(u)))
        return "".join(ans)
