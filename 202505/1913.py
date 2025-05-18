class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        can = []
        curr = []

        def dfs(i):
            if i == m:
                can.append(curr[:])
                return
            for j in range(1, 4):
                if i != 0 and curr[-1] == j:
                    continue
                curr.append(j)
                dfs(i + 1)
                curr.pop()

        dfs(0)

        @cache
        def f(mask, i):
            if i == n:
                return 1

            ans = 0
            for nm in can:
                flag = True
                for j in range(m):
                    if nm[j] == ((mask >> (j * 2)) & 3):
                        flag = False
                        break
                if flag:
                    mask2 = 0
                    for j in range(m):
                        mask2 |= nm[j] << (j * 2)
                    ans = (ans + f(mask2, i + 1)) % MOD
            return ans

        return f(0, 0)
