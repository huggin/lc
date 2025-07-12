class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:

        @cache
        def g(m, f, s):
            if f + s == m - 1:
                return [1, 1]
            if f + s > m - 1:
                return g(m, m - 1 - s, m - 1 - f)
            mi = 100
            ma = 0
            half = (m + 1) // 2

            if s < half:
                step = s - f
                for i in range(f + 1):
                    for j in range(i, i + step):
                        dp2 = g(half, i, j + 1)
                        mi = min(mi, dp2[0])
                        ma = max(ma, dp2[1])
            else:
                step = m - 1 - s - f
                k = half - (m - 1 - s)
                for i in range(f + 1):
                    for j in range(step):
                        dp2 = g(half, i, i + k + j)
                        mi = min(mi, dp2[0])
                        ma = max(ma, dp2[1])
            return [mi + 1, ma + 1]

        f, s = firstPlayer - 1, secondPlayer - 1
        if f > s:
            f, s = s, f
        return g(n, f, s)
