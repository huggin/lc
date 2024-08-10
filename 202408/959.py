class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        g = [[] for _ in range(n*n*2)]
        for i in range(n):
            for j in range(n):
                k = 2 * j + 1
                if grid[i][j] == ' ':
                    g[i*n*2+2*j].append(i*n*2+2*j+1)
                    g[i*n*2+2*j+1].append(i*n*2+2*j)
                elif grid[i][j] == '/':
                    k = 2 * j
                
                if i > 0:
                    if grid[i-1][j] == '/':
                        g[(i-1)*n*2+2*j+1].append(i*n*2+k)
                        g[i*n*2+k].append((i-1)*n*2+2*j+1)
                    else:
                        g[(i-1)*n*2+2*j].append(i*n*2+k)
                        g[i*n*2+k].append((i-1)*n*2+2*j)
                if j > 0:
                    g[i*n*2+2*j].append(i*n*2+2*j-1)
                    g[i*n*2+2*j-1].append(i*n*2+2*j)
        
        v = [0] * (n*n*2)

        def dfs(u):
            v[u] = 1
            for w in g[u]:
                if v[w] == 0:
                    dfs(w)

        ans = 0
        for i in range(n*n*2):
            if v[i] == 0:
                ans += 1
                dfs(i)
        return ans
