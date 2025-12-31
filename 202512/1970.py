class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for _ in range(row)]
        n = row * col
        parent = [i for i in range(n + 2)]
        count = [1] * (n + 2)

        def id(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            if count[u] <= count[v]:
                parent[u] = v
                count[v] += count[u]
            else:
                parent[v] = u
                count[u] += count[v]
        
        for i in range(row):
            union(i * col, n)
            union((i + 1) * col - 1, n+1)
        
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i, (r, c) in enumerate(cells):
            r -= 1
            c -= 1
            grid[r][c] = 1
            u = r * col + c
            
            for k in range(len(dx)):
                nr = r + dx[k]
                nc = c + dy[k]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    u = id(r * col + c)
                    v = id(nr * col + nc)
                    if u != v:
                        union(u, v)
            if id(n) == id(n+1):
                return i
        return -1
