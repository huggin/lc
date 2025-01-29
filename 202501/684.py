class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        id = list(range(n))
        count = [1] * n

        def find(u):
            while id[u] != u:
                id[u] = id[id[u]]
                u = id[u]
            return u

        for a, b in edges:
            i = find(a - 1)
            j = find(b - 1)
            if i == j:
                return [a, b]
            if count[i] <= count[j]:
                count[j] += count[i]
                id[i] = j
            else:
                count[i] += count[j]
                id[j] = i

        return [-1, -1]
