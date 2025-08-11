class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        a = []
        curr = 1
        while n:
            if n & 1:
                a.append(curr)
            n >>= 1
            curr <<= 1

        ps = [1]
        for c in a:
            ps.append(ps[-1] * c % MOD)

        ans = [0] * len(queries)
        for k, (l, r) in enumerate(queries):
            ans[k] = ps[r + 1] * pow(ps[l], -1, MOD) % MOD
        return ans
