class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        def f(a, m):
            a.append(1)
            a.append(m)
            a.sort()
            d = defaultdict(int)
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    d[a[j] - a[i]] += 1
            return d

        h, v = f(hFences, m), f(vFences, n)
        ans = -1
        ma = 0
        for k in h.keys():
            if k not in v:
                continue
            if k > ma:
                ma = k
                ans = k * k % MOD
        return ans
