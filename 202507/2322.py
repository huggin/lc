class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        x = [0] * n

        def dfs(u, p=0):
            ans = nums[u]
            for v in g[u]:
                if v == p:
                    continue
                ans ^= dfs(v, u)
            x[u] = ans
            return ans

        dfs(0, -1)
        self.first = 0
        self.ans = float("inf")
        self.start = False
        self.node = -1

        def dfs3(u, p):
            for v in g[u]:
                if v == p:
                    continue
                second = x[self.node] ^ x[v]
                third = x[v]
                self.ans = min(
                    self.ans,
                    max(self.first, second, third) - min(self.first, second, third),
                )
                dfs3(v, u)

        def dfs4(u, p):
            for v in g[u]:
                if v == p:
                    continue
                third = x[v]
                second = self.second ^ third
                self.ans = min(
                    self.ans,
                    max(self.first, second, third) - min(self.first, second, third),
                )
                dfs4(v, u)

        def dfs2(u, p, v1, v2):
            for v in g[u]:
                if p == v:
                    continue
                if u == v1 and v == v2 or u == v2 and v == v1:
                    self.start = True
                    self.first = x[0] ^ x[v]
                    self.node = v
                    dfs3(v, u)
                    self.first = x[v]
                    self.second = x[0] ^ x[v]
                elif not self.start:
                    dfs2(v, u, v1, v2)
                else:
                    second = x[v]
                    third = self.second ^ second
                    self.ans = min(
                        self.ans,
                        max(self.first, second, third) - min(self.first, second, third),
                    )
                    dfs4(v, u)

        for u, v in edges:
            self.start = False
            self.start2 = False
            dfs2(0, -1, u, v)

        return self.ans
