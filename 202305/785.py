class Solution:
    def dfs(self, graph, v, marked):
        for w in graph[v]:
            if marked[w] == 0:
                marked[w] = 2 if marked[v] == 1 else 1
                if not self.dfs(graph, w, marked):
                    return False
            elif marked[w] == marked[v]:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        marked = [0] * n
        for i in range(n):
            if marked[i] == 0:
                marked[i] = 1
                if not self.dfs(graph, i, marked):
                    return False

        return True
