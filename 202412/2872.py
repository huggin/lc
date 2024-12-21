class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        self.ans = 0

        def f(u, p=-1):
            ans = values[u]
            for v in tree[u]:
                if v == p:
                    continue
                ans += f(v, u)

            if ans % k == 0:
                self.ans += 1
                return 0
            return ans

        f(0)
        return self.ans
