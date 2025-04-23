class Solution:
    def countLargestGroup(self, n: int) -> int:
        def f(m):
            ans = 0
            while m > 0:
                ans += m % 10
                m //= 10
            return ans

        d = defaultdict(int)
        for i in range(1, n + 1):
            d[f(i)] += 1

        ans = 0
        ma = max(d.values())
        return sum(1 for v in d.values() if v == ma)
