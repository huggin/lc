class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        g = [[] for _ in range(n)]
        for i in range(n):
            g[favorite[i]].append(i)
        
        self.ans = 0
        visited = [-1] * n
        st = []
        s = set()
        rem = set()
        two = set()
        
        def dfs(u, k):
            visited[u] = k
            s.add(u)
            st.append(u)
            for v in g[u]:
                if visited[v] == -1:
                    dfs(v, k+1)
                elif v in s or v in rem:
                    cycle = visited[u] - visited[v] + 1
                    self.ans = max(self.ans, cycle)
                    if cycle > 2:
                        for i in range(len(st) - 1, -1, -1):
                            if st[i] in rem:
                                break
                            s.remove(st[i])
                            rem.add(st[i])
                    else:
                        two.add(u)
                        two.add(v)

            if u in s:
                s.remove(u)  
            st.pop()
        
        for u in range(n):
            if visited[u] == -1:
                dfs(u, 0)
        
        visited = [0] * n
        def dfs2(u):
            ans = 0
            visited[u] = 1
            for v in g[u]:
                if v in rem or v in two:
                    continue
                if visited[v] == 0:
                    ans = max(ans, dfs2(v))
            return ans + 1
        
        cnt = 0
        for u in two:
            cnt += dfs2(u)        

        return max(self.ans, cnt)
