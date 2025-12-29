class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = {}
        for _, y in points:
            if y not in cnt:
                cnt[y] = 1
            else:
                cnt[y] += 1

        MOD = 10**9 + 7
        a = []
        for _, v in cnt.items():
            if v > 1:
                a.append(v * (v - 1) // 2)
        tt = sum(a)
        n = len(a)
        b = [0] * n
        for i in range(n):
            b[i] = tt - a[i]

        ans = 0
        for i in range(n):
            ans = ans + a[i] * b[i]
        return ans // 2 % MOD
