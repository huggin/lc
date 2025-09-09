class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        q = [(0, 1)]
        ans = 1
        ok = 0
        j = 0
        k = 0
        for i in range(1, n):
            if q[j][0] + forget == i:
                ok -= q[j][1]
                ans -= q[j][1]
                j += 1
            if q[k][0] + delay == i:
                ok += q[k][1]
                k += 1
            ans = (ans + ok) % MOD
            q.append((i, ok))

        return ans
