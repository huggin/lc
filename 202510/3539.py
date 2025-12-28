MOD = 10**9+7

comp = [[1] * 31 for _ in range(31)]
for i in range(2, 31):
    comp[i][0] = 1
    comp[i][i] = 1
    for j in range(1, i):
        comp[i][j] = comp[i-1][j] + comp[i-1][j-1]
        if comp[i][j] >= MOD:
            comp[i][j] -= MOD

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def f(mask, m, k, i):
            if m == 0:
                if mask.bit_count() == k:
                    return 1
                return 0
            if i == n:
                return 0
            ans = f(mask>>1, m, k-(mask&1), i+1)
            for  c in range(1, m+1):
                nm = mask + c
                nk = k - (nm&1)
                nf = f(nm>>1, m-c, nk, i+1)
                ans += comp[m][c] * pow(nums[i], c, MOD) * nf % MOD
            return ans % MOD

        return f(0, m, k, 0)
